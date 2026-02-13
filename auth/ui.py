import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from .theme import *

console = Console()

# screen Utilities
def clear_screen():
    time.sleep(0.2)
    os.system("cls" if os.name == "nt" else "clear")

def sleep(t = 1):
    time.sleep(t)


#success, warn, error
def success(msg):
    console.print(msg, style = SUCCESS)

def warn(msg):
    console.print(msg, style = WARNING)

def error(msg):
    console.print(msg, style = ERROR)


#Loading 
def status(msg, t):
    with console.status(msg, spinner = "dots"):
        time.sleep(t)

def fake_loading(msg):
    for _ in track(range(30), description=msg):
        time.sleep(0.02)


#Panel and Rule
def panel(msg, title = "", style = PANEL):
    console.print(
        Panel(msg, title = title, style = style, expand= False)
    )

def rule(msg):
    console.rule(msg, style = RULE)


#Table
def display_user_table(users):
    table = Table(title = "\nRegistered Users")

    table.add_column("User Id", style = SUCCESS)
    table.add_column("Name", style = ACCENT)
    table.add_column("Email", style = WARNING)
    table.add_column("Username", style = PRIMARY)

    for uid, info in users.items():
        table.add_row(
            uid,
            info["Name"],
            info["Email"],
            info["Username"]
        )

    return table


#LOGO

def show_logo():
    logo = r"""
    """