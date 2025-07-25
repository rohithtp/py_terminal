from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown


def main():
    console = Console()
    while True:
        console.clear()
        console.print(Panel("[bold green]Welcome to Terminal Web![/bold green]\nA terminal-based UI web project.", title="Terminal Web"))
        console.print("\n[bold]Menu:[/bold]")
        console.print("[cyan]1.[/cyan] Say Hello")
        console.print("[cyan]2.[/cyan] Show Info")
        console.print("[cyan]3.[/cyan] Exit")
        console.print("[cyan]4.[/cyan] Run Bash Command")
        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4"], default="3")
        if choice == "1":
            console.print("\n[bold yellow]Hello, user![/bold yellow]\n")
            input("Press Enter to return to menu...")
        elif choice == "2":
            try:
                with open("info.md", "r") as f:
                    md_text = f.read()
                console.print(Markdown(md_text))
            except FileNotFoundError:
                console.print("[bold red]info.md file not found. Please create an info.md file in the project directory.[/bold red]")
            input("Press Enter to return to menu...")
        elif choice == "3":
            console.print("\n[bold red]Exiting... Goodbye![/bold red]")
            break
        elif choice == "4":
            import subprocess
            cmd = Prompt.ask("Enter the bash command to run (interactive)")
            console.print(f"\n[bold green]Running:[/bold green] [italic]{cmd}[/italic]\n")
            try:
                subprocess.run(cmd, shell=True)
            except Exception as e:
                console.print(f"[bold red]Error running command:[/bold red] {e}")
            input("Press Enter to return to menu...")


if __name__ == "__main__":
    main()
