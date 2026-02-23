from .ui import *

def admin_dash(users):
    admin_login(users)
    clear_screen()
    header("Admin Privileges")
    space(2)
    menu_items = [
        "View all Registered Users",
        "Delete User accounts",
        "Search user",
        "Exit"
    ]

    menu_panel(menu_items)

    choice = get_choice("Select option (1-4)")
    sleep(4)


def admin_login(users):
    clear_screen()
    header("ADMIN LOGIN")
    space()

    while True:
        admin_id = get_input("Enter Admin Username ")
        if not admin_id:
            warn("Admin ID cannot be empty!")
            continue
    
        if admin_id == users.get('A000', False):
            space()
            password = get_input("Enter password", password=True)
            if password == users.get('admin321', False):
                space()
                success_panel("Login successful")
                sleep(1)
                status("Opening Admin Dashboard...", 1)
                return
            else:
                error("Incorrect Password")
                continue
