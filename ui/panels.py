from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


console = Console()


def show_preflight(risk):
    """Render a static warning panel based on risk level. Returns a simple obj with `confirmed` attr."""
    title = "Pre-Flight Check"
    if risk.name == "SAFE":
        return type("C", (), {"confirmed": True})()

    color = "yellow"
    if risk.name == "DESTRUCTIVE":
        color = "red"
    if risk.name == "IRREVERSIBLE":
        color = "magenta"

    body = Text()
    body.append(f"Risk level: {risk.name}\n", style="bold")
    body.append("This command looks potentially dangerous. Proceed with caution.\n\n")
    body.append("(Static preflight — no LLM available yet)")

    console.print(Panel(body, title=title, style=color))

    # For MUTATING or above require explicit confirmation
    if risk.value >= 1:
        ans = Prompt.ask("Type 'yes' to proceed or anything else to abort", default="no")
        confirmed = ans.strip().lower() == "yes"
        return type("C", (), {"confirmed": confirmed})()

    return type("C", (), {"confirmed": True})()
