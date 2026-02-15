import time, os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from rich.prompt import Prompt
from .theme import *

console = Console()

# screen Utilities
def clear_screen():
    time.sleep(0.2)
    os.system("cls" if os.name == "nt" else "clear")

def sleep(seconds = 1):
    time.sleep(seconds)

def header(title, subtitle = ""):
    console.print(
        Panel(
            f"[{GLOW}]▂▃▅▇█▓▒░[/{GLOW}] [{HEADER}]{title}[/{HEADER}] [{GLOW}]░▒▓█▇▅▃▂[/{GLOW}]"
            + (f"\n[{SUBHEADER}]{subtitle}[/{SUBHEADER}]" if subtitle else ""),
            border_style=BORDER_PRIMARY,
            expand=False
        )
    )

def info_panel(content, title=""):
    console.print(
        Panel(
            content,
            title=title if title else None,
            border_style=BORDER_ACCENT,
            expand=False
        )
    )

def menu_panel(itmes, title="Menu"):
    formatted = "\n".join([f"[{PRIMARY}][{i+1}][/{PRIMARY}] {item}" for i, item in enumerate(items)])
    
    console.print(
        Panel(
            formatted,
            title=f"[{HEADER}]{title}[/{HEADER}]",
            border_style=BORDER_PRIMARY,
            expand=False
        )
    )

#success, warn, error
def success(msg):
    console.print(msg, style = SUCCESS)

def warn(msg):
    console.print(msg, style = WARNING)

def error(msg):
    console.print(msg, style = ERROR)



def info(msg):
    console.print(msg, style=INFO)

def success_panel(msg, title="SUCCESS"):
    console.print(
        Panel(
            msg,
            title=title,
            style=SUCCESS,
            border_style=BORDER_SUCCESS,
            expand=False
        )
    )

def error_panel(msg, title="ERROR"):
    console.print(
        Panel(
            msg,
            style=ERROR,
            border_style=BORDER_ERROR,
            expand=False
        )
    )

def warn_panel(msg, title= "WARNING"):
    console.print(
        Panel(
            f"[{WARNING}]{message}[/{WARNING}]",
            title=f"[{WARNING}]{title}[/{WARNING}]",
            border_style=BORDER_WARNING,
            expand=False
        )
    )


#Loading 
def status(msg, duration):
    with console.status(f"[{PRIMARY}{msg}[/{PRIMARY}]", spinner = "dots", ):
        time.sleep(duration)

def fake_loading(msg):
    for _ in track(range(30), description=f"[{PRIMARY}{msg}[/{PRIMARY}]]"):
        time.sleep(0.02)


#Panel and Rule


def rule(text = ""):
    console.rule(f"[{RULE}]{text}[/{RULE}]" if text else "", style = RULE)

def space(lines = 1):
    for _ in range(lines):
        console.print()

def get_input(prompt_text, password = False):
    if password:
        return Prompt.ask(f"[{PRIMARY}{prompt_text}[/{PRIMARY}]", password=True)
    else:
        console.print(f"[{PRIMARY}]{prompt_text}:[/{PRIMARY}]")
        return input(">>> ").strip()

def get_choice(prompt_text = "Select option"):
    console.print(f"\n{prompt_text}:", style=ACCENT)
    return input(">>> ").strip()



#Table
def display_user_table(users):
    table = Table(title = "Registered Users", style=HEADER)

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


def profile_table(user):
    table = Table(show_header=False, box=None)
#LOGO

def animated_logo():
    logo = [
        " █████╗ ██╗   ██╗████████╗██╗  ██╗",
        "██╔══██╗██║   ██║╚══██╔══╝██║  ██║",
        "███████║██║   ██║   ██║   ███████║",
        "██╔══██║██║   ██║   ██║   ██╔══██║",
        "██║  ██║╚██████╔╝   ██║   ██║  ██║",
        "╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝",
    ]

    for line in logo:
        console.print(line, style="dark_orange")
        sleep(0.05)

    console.print("\n        🔐 AUTHENTICATION SYSTEM", style="bold purple")
    console.print("              by Aryan\n", style="purple")
    sleep(0.5)