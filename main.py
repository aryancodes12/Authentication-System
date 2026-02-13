import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.login import login
from auth.ui import *
from auth.dashboard import *
from auth.sessions import *

#startup
status("Initializing Authentication System ...", 1.5)
users = load_users()

#determing the userid
if users:
    counter = max(int(u[1:]) for u in users.keys()) + 1
else: 
    counter = 1

#main loop
while True:
    clear_screen()
    panel("Authentication System")
    rule("")
    menu = """
    1. Register New User
    2. Login
    3. Exit
        """
    
    #Menu
    panel(menu, title = "Menu")
    choice = input(">>> ")

    if choice == "1":
        register_user(users, counter)
    elif choice == "2":
        user = login(users)
        clear_screen()
        if user:
            status("Starting session...", 1)
            start_session(user)

            while is_logged_in():
                current = get_current_user()
                dashboard(current)

    elif choice == "3":
        panel("👋 Thanks for using the System!")
        break
    else:
        warn("❌ Invalid Choice")

#Saving data in JSON
fake_loading("Saving data ")
save_users(users)

panel("Data Saved", style = "green")

#Displaying the present data from JSON
status("Displaying Data ....", 1)
console.print(display_user_table(users))
