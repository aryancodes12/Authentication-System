import os
from auth.storage import load_users, save_users
from auth.register import register_user
from auth.login import login
from auth.admin_dash import admin_dash

from auth.ui import (clear_screen, sleep, header, info_panel, menu_panel, 
success, success_panel, warn, warn_panel, error, error_panel, status, 
fake_loading, space, get_choice, get_input, wait_for_enter, animated_logo)

from auth.dashboard import *
from auth.sessions import *

#startup
clear_screen()
animated_logo()
space()
status("Initializing Authentication System ...", 1.5)
users = load_users()

#Checking if JSON is empty if it is then adding admin entry
if not users:
    admin_data = {
        'Name' : 'Admin',
        'Email' : 'admin@system.com',
        'Username': 'admin',
        'Password' : 'admin321'
    }

    users['A000'] = admin_data
    save_users(users)

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
    menu_items = ["Login", "Register new User", "Admin Access", "Exit"]
    
    #Menu
    menu_panel(menu_items)
    choice = get_choice("Select option (1-3)")

    if choice == "1":
        user = login(users)
        clear_screen()
        if user:
            # status("Starting session...", 1)
            start_session(user)

            while is_logged_in():
                current = get_current_user()
                user_dashboard(current, users)
        
    elif choice == "2":
        register_user(users, counter)
    elif choice == "3":
        admin_dash(users)
    elif choice == "4":
        space(2)
        fake_loading("Saving data ")
        save_users(users)

        space()

    #Displaying the present data from JSON
        status("Displaying Data ....", 1)
        space()
        # console.print(display_user_table(users))
        success_panel("👋 Thanks for using the System!")
        break
    else:
        space()
        warn("❌ Invalid Choice")


