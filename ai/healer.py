"""AI-backed failure diagnosis and healing suggestions."""

import os
import json
import re
from dataclasses import dataclass
from typing import Optional, Dict, Any

from ai.client import get_client
from ai.config import LLM_ENABLED
from ai.prompts import healing_messages


@dataclass
class HealingSuggestion:
    diagnosis: str
    suggested_command: Optional[str]
    explanation: str
    confidence: float


class Healer:
    """Produce a healing suggestion for a failed command."""

    def __init__(self, use_llm: bool = LLM_ENABLED):
        self.use_llm = use_llm
        self.client = get_client() if use_llm else None

    def diagnose(self, cmd: str, result: Dict[str, Any], cwd: Optional[str] = None) -> HealingSuggestion:
        cwd = cwd or os.getcwd()
        stderr = (result.get("stderr") or "").strip()
        returncode = result.get("returncode")

        if self.use_llm and self.client is not None:
            try:
                data = self.client.call_json(
                    messages=healing_messages(cmd, stderr, returncode or 0, cwd, os.name),
                )
                return HealingSuggestion(
                    diagnosis=str(data.get("diagnosis", "Unknown failure."))[:1000],
                    suggested_command=data.get("suggested_command"),
                    explanation=str(data.get("explanation", "No explanation provided."))[:2000],
                    confidence=float(data.get("confidence", 0.0) or 0.0),
                )
            except Exception:
                pass

        suggestion = None
        explanation = "The command failed and a safe automated fix could not be generated."
        confidence = 0.0
        diagnosis = f"Command failed with return code {returncode}."

        stderr_lower = stderr.lower()
        if "permission denied" in stderr_lower and not cmd.strip().startswith("sudo"):
            suggestion = f"sudo {cmd.strip()}"
            diagnosis = "Permission denied while executing the command."
            explanation = "The failure appears to be due to insufficient permissions. "
            explanation += "If you trust this command, rerun it with sudo."
            confidence = 0.55
        elif "command not found" in stderr_lower or "not found" in stderr_lower:
            diagnosis = "The command or executable was not found."
            explanation = "The shell could not locate the requested command. Verify the command name or install the missing tool."
            confidence = 0.25
        elif "no such file or directory" in stderr_lower:
            match = re.search(r"no such file or directory: ['\"]?([^'\"]+)['\"]?", stderr, re.IGNORECASE)
            path = match.group(1) if match else None
            if path:
                explanation = f"The path '{path}' does not exist. Check the path or create the missing file/directory."
            else:
                explanation = "A referenced file or directory could not be found. Verify the path."
            confidence = 0.3
        elif returncode == 127:
            explanation = "A required executable is missing or not available in PATH."
            confidence = 0.3

        return HealingSuggestion(
            diagnosis=diagnosis,
            suggested_command=suggestion,
            explanation=explanation,
            confidence=confidence,
        )
