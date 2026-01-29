import json
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track

os.system("clear")
console = Console()
#Variable
users = {}

#Loading the DATA from JSON
file_name = "user_data.json"
try:
    with open(file_name) as f:
        users = json.load(f)
except FileNotFoundError:
    pass
else:
    with console.status("Loading previous Data....", spinner = "moon"):
        time.sleep(1)

#Tracking the current user id from the JSON file
if users:
    counter = max(int(uid[1:]) for uid in users.keys()) + 1
else:
    counter = 1


#Alert messages
def success(msg):
    console.print(msg, style = "bold green")

def warn(msg):
    console.print(msg, style = "yellow")

def error(msg):
    console.print(msg, style = "bold red")

#Validations

def is_valid_email(email):
    return "@" in email and "." in email

def is_unique_username(username):
    return username not in [u["Username"] for u in users.values()]

#Main Function
def register_user():
    global counter

#Name
    console.print("Enter your First Name", style = "cyan")
    first_name = input(">>> ").title()
    console.print("\nEnter your Last Name", style = "cyan")
    last_name = input(">>> ").title()
    full_name = f"{first_name} {last_name}"

#Email
    while True:
        console.print("\nEnter Email Id", style = "cyan")
        email = input(">>> ")
        if is_valid_email(email):
            break
        error("Invalid email")

#Username
    while True:
        console.print("\nCreate Username", style = "cyan")
        username = input(">>> ")
        if is_unique_username(username):
            break
        warn("Username already taken")

#Password
    while True:
        console.print("\nCreate a Password", style = "cyan")
        password = input(">>> ")
        if password == username:
            warn("Password cannot match the username")
        elif len(password) < 8:
            error("Password must be of 8 character or more")
        else:
            console.print("\nConfirm the Password", style = "cyan")
            confirm = input(">>> ")
            if confirm == password:
                break
            error("Password does not match")

#ADDING DATA IN DICTONARY
    user_id = f"u{counter:03d}"
    users[user_id] = {
        "Name" : full_name,
        "Email" : email,
        "Username" : username,
        "Password" : password
        }

    counter += 1
    console.print("Registration Successful!", style = "bold green")


#MAIN LOOP
while True:
    os.system("clear")
    console.rule("[bold blue]Main Menu")
    console.print(
        Panel("👤 User Registration System", style = "Bold Cyan")
        )
    console.print("\n[bold yellow]Menu[/bold yellow]")
    console.print("1. Register User")
    console.print("2. Exit")
    choice = input(">>> ").lower()
    if choice == "1":
        register_user()
    elif choice == "2":
        console.print(
            Panel("👋 Thanks for using the System!", style = "bold red")
            )
        break
    else:
        warn("Invalid Choice")


#DATA SAVING
with open(file_name, "w") as f:
    json.dump(users, f, indent = 4)

with console.status("Saving Data ....", spinner = "moon"):
    time.sleep(1)
success("Data Saved")

#DATA DISPLAY
console.rule("[bold yellow] User's Information")
table = Table(title = "Registered Users")

table.add_column("User ID", style = "cyan")
table.add_column("Name", style = "green")
table.add_column("Email", style = "yellow")
table.add_column("Username", style = "magenta")

for  uid, info in users.items():
    table.add_row(
        uid,
        info["Name"],
        info["Email"],
        info["Username"]
     )

console.print(table)
