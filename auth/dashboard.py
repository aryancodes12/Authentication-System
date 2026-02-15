from .ui import *
from .theme import *
from .sessions import *
from .validators import validate_password

def dashboard(user):
    global username
    clear_screen()
    username = user['Username']
    header("DASHBOARD")
    space()


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
    header("Account Information")
    profile = profile_table(user)
    console.print(profile)
    space()
    wait_for_enter("Press Enter to go back")

        

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
        space()
        success_panel(f"Name updated from {old_name} to {new_name}")
        space()
        wait_for_enter()
        status("Returning to dashboard", 0.5)


def update_password(user):
    clear_screen()
    header("Update password",)
    space()
    while True:
        current = get_input("Enter current password")
        space()

        if current == user['Password']:  
            password = get_input("Create a password")
            space()
            is_valid, message = validate_password(password, current)
            console.print(message)

            if is_valid:
                space()
                confirm = get_input("Confirm password")
            
                if password == confirm:
                    user['Password'] = password
                    space()
                    success_panel("Password is Updated")
                    break
                else:
                    error("❌ Passwords don't match!")
            

    


def delete_profile(user):
    clear_screen()
    console.print("Deleting Profile Feature comming soon!", style=SUCCESS)
    space()
    wait_for_enter()
