from rich.console import Console
from rich.panel import Panel

console = Console(record=True, width=100)

console.print(Panel("[bold green]Welcome to Terminal Web![/bold green]\nA terminal-based UI web project.", title="Terminal Web"))
console.print("\n[bold]Menu Options:[/bold]")
console.print("[cyan]1.[/cyan] Say Hello")
console.print("[cyan]2.[/cyan] Show Project Info")
console.print("[cyan]3.[/cyan] Run Single Command")
console.print("[cyan]4.[/cyan] Execute Multiple Commands")
console.print("[cyan]5.[/cyan] Exit")
console.print("[cyan]6.[/cyan] Show Status")

console.print("\nEnter your choice: [yellow]3[/yellow]")
console.print("Enter the bash command to run: [yellow]rm -rf /tmp/testdir[/yellow]")
console.print("Execution mode: [yellow]capture[/yellow]")

console.print("\n[bold green]Running:[/bold green] [italic]rm -rf /tmp/testdir[/italic]\n")

# Simulate Preflight Panel
panel_content = """[bold red]Risk Level: IRREVERSIBLE[/bold red]

[bold]AI Analysis:[/bold]
This command will recursively and forcefully delete the directory '/tmp/testdir' and all its contents. 
Since '/tmp' is a system temporary directory, deleting specific folders inside it is generally safe, but any data currently in 'testdir' will be permanently lost.

[bold]Affected Resources:[/bold]
- /tmp/testdir (File System)

[bold yellow]Reversibility:[/bold yellow]
Once deleted, these files cannot be recovered easily. Ensure you no longer need them.

[bold]Are you sure you want to proceed?[/bold]"""

console.print(Panel(panel_content, title="[bold red]⚠️  PREFLIGHT WARNING ⚠️[/bold red]", border_style="red"))

console.print("\nType the command again to confirm execution: [yellow]cancel[/yellow]")
console.print("[bold yellow]Command execution cancelled.[/bold yellow]")

console.save_svg("demo_flow.svg", title="py_terminal AI Safety Net Demo")
print("Saved demo_flow.svg to current directory")
