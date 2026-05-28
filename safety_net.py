from ai.preflight import Preflight, RiskLevel
from ui.panels import show_preflight
import subprocess


preflight = Preflight()


def run(cmd: str, mode: str = "interactive"):
    """Passthrough runner with Tier-1 preflight heuristics.

    If risk is MUTATING or above, show a static warning panel and ask.
    Otherwise execute the command as before.
    """
    risk = preflight.score(cmd)
    if risk.value >= RiskLevel.MUTATING.value:
        allowed = show_preflight(risk).confirmed
        if not allowed:
            return type("R", (), {"aborted": True, "returncode": None})()

    # Execute command similarly to existing code
    try:
        if mode == "interactive":
            subprocess.run(cmd, shell=True)
            return type("R", (), {"aborted": False, "returncode": 0})()
        else:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return type("R", (), {"aborted": False, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr})()
    except Exception as e:
        return type("R", (), {"aborted": False, "returncode": -1, "error": str(e)})()
