from typing import Any, Dict

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from ai.preflight import RiskLevel


console = Console()


def _badge_text(text: str) -> Text:
    badge = Text(text, style="bold magenta")
    return badge


def _confirm_by_risk(risk: RiskLevel, command: str) -> bool:
    if risk == RiskLevel.MUTATING:
        ans = Prompt.ask(
            "Press Enter to proceed, or type 'no' to abort",
            default="yes",
        )
        return ans.strip().lower() in ("", "yes", "y")

    if risk == RiskLevel.DESTRUCTIVE:
        ans = Prompt.ask(
            "Type 'yes' to proceed with this destructive command, or anything else to abort",
            default="no",
        )
        return ans.strip().lower() == "yes"

    if risk == RiskLevel.IRREVERSIBLE:
        phrase = command.strip().split()[0] if command.strip() else "CONFIRM"
        ans = Prompt.ask(
            f"Type '{phrase}' exactly to confirm irreversible execution",
            default="",
        )
        return ans.strip() == phrase

    return True


def show_preflight(
    risk: RiskLevel,
    command: str,
    ai_summary: str | None = None,
    affected_resources: str | None = None,
    reversibility_note: str | None = None,
    ai_mode: bool = False,
):
    title = "Pre-Flight Check"
    if ai_mode:
        title += " ✨ AI"

    if risk == RiskLevel.SAFE:
        return type("C", (), {"confirmed": True})()

    color = "yellow"
    if risk == RiskLevel.DESTRUCTIVE:
        color = "red"
    if risk == RiskLevel.IRREVERSIBLE:
        color = "magenta"

    body = Text()
    body.append(f"Command: {command}\n", style="bold")
    body.append(f"Risk level: {risk.name}\n\n", style="bold")

    if ai_mode and ai_summary:
        body.append("AI Summary:\n", style="bold magenta")
        body.append(f"{ai_summary}\n\n")
    elif ai_mode:
        body.append("AI summary unavailable. Falling back to static warning.\n\n")

    if affected_resources:
        body.append("Affected resources:\n", style="bold")
        body.append(f"{affected_resources}\n\n")

    if reversibility_note:
        body.append("Reversibility note:\n", style="bold")
        body.append(f"{reversibility_note}\n\n")

    body.append("This command appears risky. Proceed with caution.")

    console.print(Panel(body, title=title, style=color))

    confirmed = _confirm_by_risk(risk, command)
    return type("C", (), {"confirmed": confirmed})()


def show_healing(suggestion: Dict[str, Any]):
    if hasattr(suggestion, "__dict__"):
        suggestion = suggestion.__dict__

    title = "Healing Suggestion ✨ AI"
    body = Text()
    body.append("Diagnosis:\n", style="bold")
    body.append(f"{suggestion.get('diagnosis', 'No diagnosis available.')}\n\n")

    if suggestion.get("suggested_command"):
        body.append("Suggested command:\n", style="bold")
        body.append(f"{suggestion['suggested_command']}\n\n")
    else:
        body.append("No safe automated command fix could be generated.\n\n")

    body.append("Explanation:\n", style="bold")
    body.append(f"{suggestion.get('explanation', '')}\n\n")
    body.append(f"Confidence: {suggestion.get('confidence', 0.0):.2f}\n")

    console.print(Panel(body, title=title, style="magenta"))

    if not suggestion.get("suggested_command"):
        return type("C", (), {"confirmed": False})()

    default_choice = "no"
    prompt = "Type 'yes' to apply the suggested fix, or anything else to skip"
    if suggestion.get("confidence", 0.0) < 0.6:
        prompt = "The fix is a best guess. Type 'yes' to apply it, or anything else to skip"

    ans = Prompt.ask(prompt, default=default_choice)
    confirmed = ans.strip().lower() == "yes"
    return type("C", (), {"confirmed": confirmed})()
