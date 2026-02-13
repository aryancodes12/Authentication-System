from .ui import *
from .theme import *
from .sessions import *

def dashboard(user):
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
        status("\nGetting info ...", 0.5)
        show_profile(user)
        sleep(2)
    elif dash_choice == "2":
        update_profile(user)
        sleep(1.5)
    elif dash_choice == "3":
        delete_profile(user)
        sleep(1.5)
    elif dash_choice == "4":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        error("Invalid choice")


def show_profile(user):
    rule("Profile")
    profile = Table(title= "")

    profile.add_column("Field", style=PRIMARY)
    profile.add_column("Value", style=ACCENT)

    profile.add_row("Name", user["Name"])
    profile.add_row("Email", user["Email"])
    profile.add_row("Username", user["Username"])
    console.print(profile)

def update_profile(user):
    panel("Update Profile Info")
    old_name = user["Name"]
    console.print(f"Current Name: {old_name}\n")
    console.print("Enter new name to update")
    new_name = input(">>> ")
    if new_name:
        user['Name'] = new_name
        console.print(f"Name updated from {old_name} to {new_name}")

def delete_profile(user):
    console.print("Deleting Profile Feature comming soon!", style=SUCCESS)