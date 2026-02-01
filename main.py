import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.ui import console, success, warn, error, status, panel, table, rule


status("Loading ....")
users = load_users()
if users:
    counter = max(int(u[1:]) for u in users.keys()) + 1
else: 
    counter = 1

while True:
    os.system("clear") # for linux
    #os.system("cls") # for windows
    panel("Authentication System", "blue")
    rule("Main Menu")
    console.print("1. Register User")
    console.print("2. Exit")
    choice = input(">>> ")

    if choice == "1":
        register_user(users, counter)
    elif choice == "2":
        panel("👋 Thanks for using the System!")
        break
    else:
        warn("Invalid Choice")

save_users(users)
status("Saving Data ....")

panel("Data Saved", "green")

status("Displaying Data ....")
console.print(table(users))
