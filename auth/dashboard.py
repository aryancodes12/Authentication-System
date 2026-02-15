from .ui import *
from .theme import *
from .sessions import *

def dashboard(user):
    clear_screen()

    header("DASHBOARD", f"Welcome back {user['Username']}")

    menu_items = [
        "View Profile",
        "Update Name",
        "Change Password",
        "Delete Account",
        "Logout"
    ] 

    menu_panel(menu_items, title="Quick Actions")
    

    dash_choice = get_choice("Select option (1-5)")

    if dash_choice == "1":
        show_profile(user)
    elif dash_choice == "2":
        update_profile(user)
        
    elif dash_choice == "3":
        update_password(user)
        status("Returning to dashboard", 5)
    elif dash_choice == "4":
        delete_profile(user)
    elif dash_choice == "5":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        error("Invalid choice")


def show_profile(user):
    clear_screen()
    status("Loading information...", 0.6)
    rule("Profile")
    profile = profile_table(user)
    console.print(profile)
    wait_for_enter("Press Enter to go back")
    # panel("Press Enter to go back")
    # key = input("")
    # if not key:
    #     return None
        

def update_profile(user):
    clear_screen()
    header("Update Name")
    old_name = user["Name"]
    space()
    info(f"Current Name: {old_name}")

    # console.print("Enter new name to update", style = "cyan")
    new_name = get_input("Enter new name to update")
    space()
    if new_name:
        user['Name'] = new_name
        success_panel(f"Name updated from {old_name} to {new_name}")
        sleep(1)
        status("Returning to dashboard", 0.6)


def update_password(user):
    clear_screen()
    header("Update password",)
    space()
    while True:
        current = get_input("Enter current password")

        if current == user['Password']:
            new_pass = get_input("Create new Password")

            if new_pass != current:
                confirm = get_input("Confirm the password")
        elif current != user['Password']:
            error("Incorrect Password")

    


def delete_profile(user):
    console.print("Deleting Profile Feature comming soon!", style=SUCCESS)
