import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.ui import console, success, warn, error, loading, panel

os.system("clear") # for linux
#os.system("cls") # for windows

loading("Loading ....")
users = load_users()
if users:
    counter = max(int(u[1:]) for u in users.keys()) + 1
else: 
    counter = 1

while True:
    panel("Authentication System")
    console.rule("Main Menu", style = "bold blue")
    console.print("1. Register User")
    console.print("2. Exit")
    choice = input(">>> ")

    if choice == "1":
        register_user(users, counter)
    elif choice == "2":
        break
    else:
        warn("Invalid Choice")

save_users(users)
loading("Saving Data ....")

success("Data Saved")
