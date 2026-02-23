from .ui import *

def admin_dash(users):
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

    if not choice:
        space()
        warn("Invalid choice")
        space(2)
        wait_for_enter()
        return None

    if choice == '1':
        clear_screen()
        show_users(users)
    elif choice == "4":
        return None

    


def admin_login(users):
    clear_screen()
    header("ADMIN LOGIN page")
    space()

    #Username
    while True:
        username = get_input("Enter Admin Username  ('q' to quit)")


        if username == "q":
            return None

        user = None
        for u in users.values():
            if u["Username"].lower() == username or u["Email"] == username:
                user = u
                break
        if not user:
            space()
            error_panel("User not Found")
            space(2)
            wait_for_enter()
            return None

        #Password input
        attempts = 3
        while attempts > 0:
            space()
            warn_panel(f"{attempts} attempts left")
            password = get_input("Password", password=True)

            if password == user["Password"]:
                space(2)
                success_panel(f"Welcome back, {user['Name']}!")
                space()
                status("Starting session...", 1)
                return user
            else:
                attempts -= 1
                if attempts > 0:
                    space()
                    error_panel(f"Incorrect password! {attempts} attempts remaining")
                else:
                    space()
                    error_panel("Too many failed attempts")
                    status("Returning to main menu...", 1)
                    return None

def show_users(users):
    clear_screen()
    status("Loading information...", 0.4)
    header("REGISTERED USERS")
    profile = display_user_table(users)
    console.print(profile)
    space()
    choice = get_choice("Enter 'q' to return")
    if choice == 'q':
        return
    