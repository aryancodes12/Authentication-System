from auth.register import register_user
from auth.login import login
from auth.admin_dash import admin_dash
from auth.admin import admin_login

from auth.ui import (clear_screen, header, menu_panel, 
success_panel, warn, status, space, get_choice, animated_logo)

from auth.dashboard import user_dashboard
from auth.sessions import start_session, is_logged_in, get_current_user

from database.connect import create_database, create_users_table

#startup
clear_screen()
animated_logo()
space()
status("Initializing Authentication System ...", 1.5)

#Creating database and users table if not exists
create_database()
create_users_table()


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
        #remove the users argument from login fucn
        user = login()
        clear_screen()
        if user:
            start_session(user)

            while is_logged_in():
                current = get_current_user()
                user_dashboard(current)
        
    elif choice == "2":
        register_user()

    elif choice == "3":
        admin = admin_login()
        clear_screen()
        if admin:
            start_session(admin)
            while is_logged_in():
                admin_dash()
    elif choice == "4":

        space()
        success_panel("👋 Thanks for using the System!")
        break

    else:
        space()
        warn("❌ Invalid Choice")
        continue