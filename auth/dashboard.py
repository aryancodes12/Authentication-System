from .ui import *
from .theme import *
from .sessions import *
from rich.layout import Layout

def dashboard(user):
    layout = Layout()

    layout.split_column(
        Layout(name = "header", size = 3),
        Layout(name = "actions", size= 8)
    )


    header_text = f"Welcome back, {user['Name']}!"
    layout['header'].update(
        create_panel(
            header_text,
            title= "Dashboard",
            style = "bold bright_cyan",
            border_style= "bright_cyan"
        )
    )

    actions = f"""
    [1] View Profile
    [2] Update Name
    [3] Delete Account
    [4] Logout
    """

    layout['actions'].update(
        create_panel(
            actions,
            title="Choose action",
            subtitle= "Press number",
            border_style= "bright_green"
        )
    )



    console.clear()
    console.print(layout)

    choice = input(">>> ")

    if choice == "1":
        status("\nGetting info ...", 0.5)
        show_profile(user)
    elif choice == "2":
        update_profile(user)
        status("Returning to dashboard", 0.6)
    elif choice == "3":
        delete_profile(user)
        status("Returning to dashboard", 0.6)
    elif choice == "4":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        error("Invalid choice")



def show_profile(user):
    clear_screen()
    rule("Profile")
    profile = Table(title= "")

    profile.add_column("Field", style=PRIMARY)
    profile.add_column("Value", style=ACCENT)

    profile.add_row("Name", user["Name"])
    profile.add_row("Email", user["Email"])
    profile.add_row("Username", user["Username"])
    console.print(profile)

    panel("Enter 'q' to go back")
    while True:
        key = input(">>> ")
        if key == "q":
            status("Returning to dashboard", 0.6)
            dashboard(user)
            break
        else:
            error("Invalid choice")

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

def delete_profile(user):
    console.print("Deleting Profile Feature comming soon!", style=SUCCESS)