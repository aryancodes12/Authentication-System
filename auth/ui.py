import time
from rich.console import Console

console = Console()

def success(msg):
    console.print(msg, style = "bold green")

def warn(msg):
    console.print(msg, style = "yellow")

def error(msg):
    console.print(msg, style = "bold red")

def loading(msg):
    with console.status(msg, spinner = "moon"):
        time.sleep(1)
