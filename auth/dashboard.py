from .ui import *
from .theme import *
from .sessions import *
from .validators import validate_password
from .storage import save_users

def user_dashboard(user, users):
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
        show_user_profile(user)
    elif dash_choice == "2":
        update_user_profile_name(user, users)
        
    elif dash_choice == "3":
        update_user_password(user, users)
        status("Returning to dashboard", 1)
    elif dash_choice == "4":
        delete_user_profile(user, users)
    elif dash_choice == "5":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        error("Invalid choice")


def show_user_profile(user):
    clear_screen()
    status("Loading information...", 0.6)
    header("Account Information")
    profile = profile_table(user)
    console.print(profile)
    space()
    wait_for_enter("Press Enter to go back")

        

def update_user_profile_name(user, users):
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
        save_users(users)
        space()
        success_panel(f"Name updated from {old_name} to {new_name}")
        space()
        wait_for_enter()
        status("Returning to dashboard", 0.5)


def update_user_password(user, users):
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
                    save_users(users)
                    space()
                    success_panel("Password is Updated")
                    break
                else:
                    error("❌ Passwords don't match!")
            

    


def delete_user_profile(user, users):
    clear_screen()
    header("DELETE ACCOUNT")
    space()
    warn_panel("PERMANENT DELETION WARNING \n\n"
    "By performing this action, you are permenently\n"
    "deleting your account. This action CANNOT be undone.\n\n"
    f"Account to be deleted:\n"
    f"- Name: {user['Name']}\n"
    f"- Username: {user['Username']}\n"
    f"- Email: {user['Email']}\n",
    title="WARNING"
    )
    space()

    password = get_input("Enter password to verify", password=True)

    if password != user['Password']:
        space()
        error_panel("Incorrect password!\nDeletion cancelled for security.")
        sleep(2)
        return

    space()
    error_panel("Enter 'DELETE' to confirm the account deletation")
    space()

    confirm = get_input("Confirmation")

    if not confirm:
        space()
        warn("No input provided, Cancelling the process")
        sleep(1.5)
        return
    
    if confirm != "DELETE":
        warn("Confirmation command didn't match. Cancelling the process.")
        sleep(1.5)
        return
    
    username = user['Username']
    user_id_to_delete = None

    for uid, user_data in users.items():
        if user_data['Username'] == username:
            user_id_to_delete = uid
            break
    
    if user_id_to_delete:
        del users[user_id_to_delete]

        save_users(users)
        space()

        success_panel(
            "Account Deleted Successfully!\n\n"
            f"User '{username} has been permanently removed.\n'"
            "Thank you for using our system."
        )
        space()

        end_session()

        status("Returning to main menu...", 2)
    else:
        space()
        error_panel("Error: User not found in database!")
        sleep(2)

