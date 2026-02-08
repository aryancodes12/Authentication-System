import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.login import login
from auth.ui import console, success, warn, error, status, panel, display_user_table, rule, page


status("Loading ....")
users = load_users()
if users:
    counter = max(int(u[1:]) for u in users.keys()) + 1
else: 
    counter = 1

while True:
    page()
    panel("Authentication System")
    rule("")
    menu = """
    1. Register New User
    2. Login
    3. Exit
        """
    panel(menu, title = "Menu")
    choice = input(">>> ")

    if choice == "1":
        register_user(users, counter)
    elif choice == "2":
        user = login(users)
    elif choice == "3":
        panel("👋 Thanks for using the System!")
        break
    else:
        warn("Invalid Choice")

save_users(users)
status("Saving Data ....")

panel("Data Saved", style = "green")

status("Displaying Data ....")
console.print(display_user_table(users))
