from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
import subprocess
import signal
import time
import sys
from pathlib import Path

# Ensure project root is on sys.path so sibling modules (e.g. safety_net)
# can be imported when running this file as a script.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from safety_net import run as safety_run
# Defer importing `status_capture` until needed to avoid import issues when
# running this file as a script (ensures package resolution works).
gather_status = None
print_status = None


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
        console.print("[cyan]6.[/cyan] Show Status")
        
        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5", "6"], default="5")
        if choice == "1":
            console.print("\n[bold yellow]Hello, user![/bold yellow]\n")
            input("Press Enter to return to menu...")
        elif choice == "2":
            try:
                with open("docs/info.md", "r") as f:
                    md_text = f.read()
                console.print(Markdown(md_text))
            except FileNotFoundError:
                console.print("[bold red]docs/info.md file not found. Please create an info.md file in the docs directory.[/bold red]")
            input("Press Enter to return to menu...")
        elif choice == "3":
            cmd = Prompt.ask("Enter the bash command to run")
            console.print(f"\n[bold green]Running:[/bold green] [italic]{cmd}[/italic]\n")
            
            # Ask user for execution mode
            mode = Prompt.ask("Execution mode", choices=["interactive", "capture"], default="interactive")
            
            try:
                if mode == "interactive":
                    console.print("[yellow]Running in interactive mode (use Ctrl+C to stop long-running commands)[/yellow]\n")
                    res = safety_run(cmd, mode="interactive")
                else:
                    console.print("[yellow]Running in capture mode (output will be displayed after completion)[/yellow]\n")
                    result = safety_run(cmd, mode="capture")
                    if getattr(result, "stdout", None):
                        console.print(f"[green]Output:[/green]\n{result.stdout}")
                    if getattr(result, "stderr", None):
                        console.print(f"[yellow]Errors:[/yellow]\n{result.stderr}")
                    if getattr(result, "returncode", 0) != 0:
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
                            res = safety_run(cmd, mode="interactive")
                        else:
                            console.print(f"[yellow]Running command {i} in capture mode...[/yellow]")
                            result = safety_run(cmd, mode="capture")
                            if getattr(result, "stdout", None):
                                console.print(f"[green]Output:[/green]\n{result.stdout}")
                            if getattr(result, "stderr", None):
                                console.print(f"[yellow]Errors:[/yellow]\n{result.stderr}")
                            if getattr(result, "returncode", 0) != 0:
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
        elif choice == "6":
            console.print('\n[bold blue]Status Capture:[/bold blue]\n')
            try:
                # Load the status_capture module directly from file to avoid
                # package import issues when running this script directly.
                import runpy
                import types
                from pathlib import Path

                pkg_dir = Path(__file__).resolve().parent
                file_path = pkg_dir.joinpath('status_capture.py')
                module_dict = runpy.run_path(str(file_path))
                mod = types.SimpleNamespace(
                    gather_status=module_dict.get('gather_status'),
                    print_status=module_dict.get('print_status'),
                )

                if not getattr(mod, 'gather_status', None) or not getattr(mod, 'print_status', None):
                    raise RuntimeError('required functions not found in status_capture')

                status = mod.gather_status('.')
                mod.print_status(status)
            except Exception as e:
                console.print(f'[bold red]Status capture utility not available:[/bold red] {e}')
            input("Press Enter to return to menu...")


if __name__ == "__main__":
    main()
