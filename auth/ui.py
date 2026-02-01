import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def success(msg):
    console.print(msg, style = "bold green")

def warn(msg):
    console.print(msg, style = "yellow")

def error(msg):
    console.print(msg, style = "bold red")

def status(msg):
    with console.status(msg, spinner = "dots"):
        time.sleep(1)

def panel(msg, style = "blue"):
    console.print(
        Panel(msg, style = style)
    )

def rule(msg):
    console.rule(msg, style = "bold blue")

def table(users):
    table = Table(title = "\nRegistered Users")

    table.add_column("User Id", style = "cyan")
    table.add_column("Name", style = "green")
    table.add_column("Email", style = "yellow")
    table.add_column("Username", style = "magenta")

    for uid, info in users.items():
        table.add_row(
            uid,
            info["Name"],
            info["Email"],
            info["Username"]
        )

    return table