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
    profile = Table(title= "")

    profile.add_column("Field", style=PRIMARY)
    profile.add_column("Value", style=ACCENT)

    profile.add_row("Name", user["Name"])
    profile.add_row("Email", user["Email"])
    profile.add_row("Username", user["Username"])
    console.print(profile)

    panel("Press Enter to go back")
    key = input("")
    if not key:
        return None
        

def update_profile(user):
    clear_screen()
    panel("Update Profile Info")
    old_name = user["Name"]
    console.print(f"Current Name: {old_name}\n", style= PRIMARY)
    console.print("Enter new name to update", style = "cyan")
    new_name = input(">>> ")
    if new_name:
        user['Name'] = new_name
        panel(f"Name updated from {old_name} to {new_name}")
        sleep(1)
        status("Returning to dashboard", 0.6)


def update_password(user):
    clear_screen()
    msg = f"""
    Update your current password
    Enter current password to begin
    """
    panel(msg, title = "Update Password")
    while True:
        current = input(">>> ")

        if current == user['Password']:
            panel("Create new password")
            new_pass = input(">>> ")

            if new_pass != current:
                panel("Confirm the password")
                confirm = input(">>> ")
        elif current != user['Password']:
            error("Incorrect Password")

    


def delete_profile(user):
    console.print("Deleting Profile Feature comming soon!", style=SUCCESS)
