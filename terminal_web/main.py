from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def main():
    console = Console()
    while True:
        console.clear()
        console.print(Panel("[bold green]Welcome to Terminal Web![/bold green]\nA terminal-based UI web project.", title="Terminal Web"))
        console.print("\n[bold]Menu:[/bold]")
        console.print("[cyan]1.[/cyan] Say Hello")
        console.print("[cyan]2.[/cyan] Show Info")
        console.print("[cyan]3.[/cyan] Exit")
        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3"], default="3")
        if choice == "1":
            console.print("\n[bold yellow]Hello, user![/bold yellow]\n")
            input("Press Enter to return to menu...")
        elif choice == "2":
            console.print("\n[bold magenta]This is a demo terminal web app using Rich.[/bold magenta]\n")
            input("Press Enter to return to menu...")
        elif choice == "3":
            console.print("\n[bold red]Exiting... Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main()
