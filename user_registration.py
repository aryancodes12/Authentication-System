import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
#Variable
users = {}

#Loading the DATA from JSON
file_name = "user_data.json"
try:
    with open(file_name) as f:
        users = json.load(f)
except FileNotFoundError:
    console.print("File does not exist", style="bold red")
else:
    print("Previous data is loaded")

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
    first_name = input("Enter your first name: ").title()
    last_name = input("Enter your last name: ").title()
    full_name = f"{first_name} {last_name}"

#Email
    while True:
        email = input("Enter Email Id: ")
        if is_valid_email(email):
            break
        error("Invalid email")

#Username
    while True:
        username = input("Create username: ")
        if is_unique_username(username):
            break
        warn("Username already taken")

#Password
    while True:
        password = input("Create a password: ")
        if password == username:
            warn("Password cannot match the username")
        elif len(password) < 8:
            error("Password must be of 8 character or more")
        else:
            confirm = input("Confirm the password: ")
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
    console.print(
        Panel("Registration Successful!", style = "bold green")
        )


#MAIN LOOP
while True:
    console.print(
        Panel("User Registration System", style = "Bold Cyan")
        )
    console.print("\n[bold yellow]Menu[/bold yellow]")
    
    console.print("1. Register User")
    console.print("2. Exit")
    choice = input(">>>").lower()
    if choice == "1":
        register_user()
    elif choice == "2":
        error("\nExiting the Program")
        break
    else:
        warn("Invalid Choice")


#DATA SAVING
with open(file_name, "w") as f:
    json.dump(users, f, indent = 4)

console.print("\nData saved successfully", style = "Bold Green")

#DATA DISPLAY
#for user, info in users.items():
   # console.print(user, style = "Purple")
   # for k, v in info.items():
    #    console.print(f"{k} : {v}")
   # print()

table = Table(title = "Registered Users")

table.add_column("User ID", style = "cyan")
table.add_column("Name")
table.add_column("Email")
table.add_column("Username")
table.add_column("Password")

for  uid, info in users.items():
    table.add_row(
        uid,
        info["Name"],
        info["Email"],
        info["Username"],
        info["Password"]
     )

console.print(table)
