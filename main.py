import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.login import login
from auth.ui import console, success, warn, error, status, panel, display_user_table, rule, page, dashboard_menu
from auth.sessions import start_session, end_session, get_current_user, is_logged_in


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
        if user:
            start_session(user)

            while is_logged_in():
                current = get_current_user()

                dashboard_menu(current)
                dash_choice = input(">>> ")

                if dash_choice == "1":
                    panel(f"Name: {current['Name']}\n" f"Email: {current['Email']}\n"
                    f"Username: {current['Username']}")

                elif dash_choice == "2":
                    end_session()
                    success("Logged Out successfully")

                else:
                    error("Invalid choice")
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
