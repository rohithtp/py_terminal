from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
import subprocess
import signal
import time


def main():
    console = Console()
    while True:
        console.clear()
        console.print(Panel("[bold green]Welcome to Terminal Web![/bold green]\nA terminal-based UI web project.", title="Terminal Web"))
        console.print("\n[bold]Menu Options:[/bold]")
        console.print("\n[bold blue]Basic Operations:[/bold blue]")
        console.print("[cyan]1.[/cyan] Say Hello")
        console.print("[cyan]2.[/cyan] Show Project Info")
        console.print("\n[bold blue]Command Execution:[/bold blue]")
        console.print("[cyan]3.[/cyan] Run Single Command")
        console.print("[cyan]4.[/cyan] Execute Multiple Commands")
        console.print("\n[bold blue]System:[/bold blue]")
        console.print("[cyan]5.[/cyan] Exit")
        
        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5"], default="5")
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
            cmd = Prompt.ask("Enter the bash command to run")
            console.print(f"\n[bold green]Running:[/bold green] [italic]{cmd}[/italic]\n")
            
            # Ask user for execution mode
            mode = Prompt.ask("Execution mode", choices=["interactive", "capture"], default="interactive")
            
            try:
                if mode == "interactive":
                    console.print("[yellow]Running in interactive mode (use Ctrl+C to stop long-running commands)[/yellow]\n")
                    subprocess.run(cmd, shell=True)
                else:
                    console.print("[yellow]Running in capture mode (output will be displayed after completion)[/yellow]\n")
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
                    if result.stdout:
                        console.print(f"[green]Output:[/green]\n{result.stdout}")
                    if result.stderr:
                        console.print(f"[yellow]Errors:[/yellow]\n{result.stderr}")
                    if result.returncode != 0:
                        console.print(f"[bold red]Command failed with exit code {result.returncode}[/bold red]")
            except subprocess.TimeoutExpired:
                console.print("[bold red]Command timed out after 30 seconds[/bold red]")
            except KeyboardInterrupt:
                console.print("\n[bold yellow]Command interrupted by user[/bold yellow]")
            except Exception as e:
                console.print(f"[bold red]Error running command:[/bold red] {e}")
            input("Press Enter to return to menu...")
        elif choice == "4":
            console.print("\n[bold cyan]Multiple Commands Execution[/bold cyan]")
            console.print("Enter commands one by one. Type 'done' when finished, or 'cancel' to abort.\n")
            
            commands = []
            while True:
                cmd = Prompt.ask("Enter command (or 'done'/'cancel')")
                if cmd.lower() == 'done':
                    break
                elif cmd.lower() == 'cancel':
                    console.print("[bold yellow]Operation cancelled.[/bold yellow]")
                    input("Press Enter to return to menu...")
                    break
                elif cmd.strip():
                    commands.append(cmd.strip())
                else:
                    console.print("[bold red]Please enter a valid command.[/bold red]")
            
            if commands:
                console.print(f"\n[bold green]Executing {len(commands)} commands:[/bold green]\n")
                for i, cmd in enumerate(commands, 1):
                    console.print(f"[bold cyan]Command {i}:[/bold cyan] [italic]{cmd}[/italic]")
                    
                    # Ask for execution mode for each command
                    mode = Prompt.ask(f"Mode for command {i}", choices=["interactive", "capture"], default="capture")
                    
                    try:
                        if mode == "interactive":
                            console.print(f"[yellow]Running command {i} in interactive mode...[/yellow]")
                            subprocess.run(cmd, shell=True)
                        else:
                            console.print(f"[yellow]Running command {i} in capture mode...[/yellow]")
                            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
                            if result.stdout:
                                console.print(f"[green]Output:[/green]\n{result.stdout}")
                            if result.stderr:
                                console.print(f"[yellow]Errors:[/yellow]\n{result.stderr}")
                            if result.returncode != 0:
                                console.print(f"[bold red]Command failed with exit code {result.returncode}[/bold red]")
                        console.print("-" * 50)
                    except subprocess.TimeoutExpired:
                        console.print(f"[bold red]Command {i} timed out after 30 seconds[/bold red]")
                        console.print("-" * 50)
                    except KeyboardInterrupt:
                        console.print(f"\n[bold yellow]Command {i} interrupted by user[/bold yellow]")
                        console.print("-" * 50)
                    except Exception as e:
                        console.print(f"[bold red]Error running command {i}:[/bold red] {e}")
                        console.print("-" * 50)
                
                console.print("\n[bold green]All commands completed![/bold green]")
            input("Press Enter to return to menu...")
        elif choice == "5":
            console.print("\n[bold red]Exiting... Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main()
