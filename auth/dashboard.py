from .ui import *
from .theme import *
from .sessions import *

def dashboard(user):
    clear_screen()
    rule("Dashboard")

    panel(f"Welcome back {user['Username']}")

    menu = Table(title= "")

    menu.add_column("Option", style=ACCENT, justify= "center")
    menu.add_column("Action", style="magenta",)

    menu.add_row("1", "View Profile")
    menu.add_row("2", "Update Profile")
    menu.add_row("3", "Delete Profile")
    menu.add_row("4", "Logout")
    console.print(menu)

    dash_choice = input(">>> ")

    if dash_choice == "1":
        show_profile(user)
    elif dash_choice == "2":
        update_profile(user)
        # status("Returning to dashboard", 0.6)
    elif dash_choice == "3":
        update_password(user)
        status("Returning to dashboard", 5)
    elif dash_choice == "4":
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
    panel("Update your current password", title = "Update Password")

    


def delete_profile(user):
    console.print("Deleting Profile Feature comming soon!", style=SUCCESS)
