import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.login import login
from auth.ui import *
from auth.dashboard import *
from auth.sessions import *

#startup
clear_screen()
animated_logo()
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
    header("Authentication System")
    space()
    menu_items = ["Login", "Register new User", "Exit"]
    
    #Menu
    menu_panel(menu_items)
    choice = get_choice("Select option (1-3)")

    if choice == "1":
        user = login(users)
        clear_screen()
        if user:
            status("Starting session...", 1)
            start_session(user)

            while is_logged_in():
                current = get_current_user()
                dashboard(current)
        
    elif choice == "2":
        register_user(users, counter)
    elif choice == "3":
        space()
        success_panel("👋 Thanks for using the System!")
        break
    else:
        space()
        warn("❌ Invalid Choice")

#Saving data in JSON
space(2)
fake_loading("Saving data ")
save_users(users)

space()

#Displaying the present data from JSON
status("Displaying Data ....", 1)
space()
console.print(display_user_table(users))
