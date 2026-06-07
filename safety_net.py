from dataclasses import dataclass
import subprocess
import os
from typing import Optional

from ai.preflight import Preflight, RiskLevel
from ai.client import get_client
from ai.config import LLM_ENABLED, OFFLINE_MODE, validate_config
from ai.prompts import preflight_messages
from ai.healer import Healer
from ui.panels import show_preflight, show_healing


@dataclass
class Result:
    aborted: bool = False
    returncode: Optional[int] = None
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    error: Optional[str] = None
    cmd: Optional[str] = None

    @property
    def failed(self) -> bool:
        return not self.aborted and self.returncode is not None and self.returncode != 0


preflight = Preflight()


def _fetch_ai_preflight(command: str) -> dict[str, str] | None:
    if not LLM_ENABLED or OFFLINE_MODE:
        return None
    try:
        client = get_client()
        return client.call_json(messages=preflight_messages(command))
    except Exception:
        return None


def _execute(cmd: str, mode: str) -> Result:
    try:
        if mode == "interactive":
            proc = subprocess.run(cmd, shell=True)
            return Result(aborted=False, returncode=proc.returncode, cmd=cmd)

        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return Result(
            aborted=False,
            returncode=proc.returncode,
            stdout=proc.stdout,
            stderr=proc.stderr,
            cmd=cmd,
        )
    except subprocess.TimeoutExpired as exc:
        return Result(
            aborted=False,
            returncode=-1,
            stdout=getattr(exc, "stdout", None),
            stderr=getattr(exc, "stderr", None),
            error="Command timed out after 30 seconds",
            cmd=cmd,
        )
    except Exception as exc:
        return Result(
            aborted=False,
            returncode=-1,
            error=str(exc),
            cmd=cmd,
        )


def run(cmd: str, mode: str = "interactive", recursion_depth: int = 0) -> Result:
    if recursion_depth >= 2:
        return Result(aborted=False, error="Maximum healing recursion reached.", cmd=cmd)

    if not validate_config():
        return Result(aborted=True, error="LLM configuration invalid.", cmd=cmd)

    risk = preflight.score(cmd)
    ai_details = None
    if risk.value >= RiskLevel.MUTATING.value:
        ai_details = _fetch_ai_preflight(cmd)
        if ai_details:
            summary = ai_details.get("plain_english_summary")
            resources = ai_details.get("affected_resources")
            reversal = ai_details.get("reversibility_note")
            allowed = show_preflight(
                risk,
                cmd,
                ai_summary=summary,
                affected_resources=resources,
                reversibility_note=reversal,
                ai_mode=True,
            ).confirmed
        else:
            allowed = show_preflight(risk, cmd, ai_mode=False).confirmed

        if not allowed:
            return Result(aborted=True, cmd=cmd)

    result = _execute(cmd, mode)
    if result.failed and mode == "capture":
        healer = Healer()
        fix = healer.diagnose(cmd, {"stderr": result.stderr, "returncode": result.returncode})
        if fix.suggested_command:
            apply_fix = show_healing(fix.__dict__).confirmed
            if apply_fix:
                return run(fix.suggested_command, mode=mode, recursion_depth=recursion_depth + 1)

    return result
