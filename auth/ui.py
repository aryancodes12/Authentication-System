import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def success(msg):
    console.print(msg, style = "bold green")

def warn(msg):
    console.print(msg, style = "yellow")

def error(msg):
    console.print(msg, style = "bold red")

def loading(msg):
    with console.status(msg, spinner = "star"):
        time.sleep(1)

def panel(msg):
    console.print(
        Panel(msg, style = "blue")
    )