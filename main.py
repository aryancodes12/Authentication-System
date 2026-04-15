import os
from auth.storage import load_users, save_users, admin_data
from auth.register import register_user
from auth.login import login
from auth.admin_dash import admin_dash, admin_login

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
    admin_data(users)
    
    

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
    choice = get_choice("Select option (1-4)")

    if choice == "1":
        user = login(users)
        clear_screen()
        if user:
            start_session(user)

            while is_logged_in():
                current = get_current_user()
                user_dashboard(current, users)
        
    elif choice == "2":
        register_user(users, counter)
    elif choice == "3":
        admin = admin_login(users)
        clear_screen()
        if admin:
            start_session(admin)
            while is_logged_in():
                admin_dash(users)
    elif choice == "4":
        space(2)
        fake_loading("Saving data ")
        save_users(users)

        space()

        space()
        success_panel("👋 Thanks for using the System!")
        break
    else:
        space()
        warn("❌ Invalid Choice")


