import json
from rich.console import Console

console = Console()

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
users = {}
if users:
    counter = max(int(uid[1:]) for uid in users.keys()) + 1
else:
    counter = 1

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
        console.print("Invalid Email format", style = "Red")

#Username
    while True:
        username = input("Create username: ")
        if is_unique_username(username):
            break
        console.print("Username already taken", style = "Red")

#Password
    while True:
        password = input("Create a password: ")
        if password == username:
            console.print("Password cannot match the username", style = "Red")
        elif len(password) < 8:
            console.print("Password must be atleast 8 characters", style = "Red")
        else:
            confirm = input("Confirm the password: ")
            if confirm == password:
                break
            console.print("Password do not match", style = "Red")

#ADDING DATA IN DICTONARY
    user_id = f"u{counter:03d}"
    users[user_id] = {
        "Name" : full_name,
        "Email" : email,
        "Username" : username,
        "Password" : password
        }

    counter += 1
    console.print("\nRegisteration Successful\n", style = "Green")


#MAIN LOOP
while True:
    choice = input("Register new user? (y/n): ").lower()
    if choice == "y":
        register_user()
    elif choice == "n":
        break
    else:
        console.print("Invalid choice", style = "Yellow")


#DATA SAVING
with open(file_name, "w") as f:
    json.dump(users, f, indent = 4)

console.print("\nData saved successfully", style = "Bold Green")

#DATA DISPLAY
for user, info in users.items():
    console.print(user, style = "Purple")
    for k, v in info.items():
        console.print(f"{k} : {v}")
    print()
