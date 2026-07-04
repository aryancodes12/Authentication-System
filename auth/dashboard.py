import bcrypt
from .ui import *
from .theme import *
from .sessions import *
from .validators import validate_password
from database.select import select_one_user_info
from database.update import update_user_name, update_user_password
from database.delete import delete_user

def user_dashboard(user):
    global username
    global user_info
    user_info = select_one_user_info(user)
    clear_screen()
    username = user_info['username']
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
        show_user_profile(user_info)
    elif dash_choice == "2":
        update_user_profile_name(user_info)
        
    elif dash_choice == "3":
        update_user_pass(user_info)
        status("Returning to dashboard", 1)
    elif dash_choice == "4":
        delete_user_profile(user_info)
    elif dash_choice == "5":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        warn("Invalid choice")


def show_user_profile(user_info):
    clear_screen()
    status("Loading information...", 0.6)
    header("Account Information")
    profile = profile_table(user_info)
    console.print(profile)
    space()
    wait_for_enter("Press Enter to go back")


def update_user_profile_name(user_info):
    clear_screen()
    header("Update Name")
    old_name = user_info["name"]
    space()
    info(f"Current Name: {old_name}")

    new_name = get_input("Enter new name to update").strip()
    space()
    if new_name:
        update_user_name(old_name, new_name)
        space()
        success_panel(f"Name updated from {old_name.title()} to {new_name.title()}")
        space()
        wait_for_enter()
        status("Returning to dashboard", 0.5)


def update_user_pass(user_info):
    clear_screen()
    header("Update password",)
    space()
    while True:
        user_email = get_input("Enter Email ('q' to quit) ")
        if user_email == 'q':
            return None
        space()

        if user_email == user_info['email']:  
            password = get_input("Create a password ")
            space()
            is_valid, message = validate_password(password, user_email)
            console.print(message)

            if is_valid:
                space()
                new_password = get_input("Confirm password")
            
                if password == new_password:
                    hashed_new_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    update_user_password(hashed_new_password, user_email)
                    space()
                    success_panel("Password is Updated")
                    break
                else:
                    error("❌ Passwords don't match!")



def delete_user_profile(user_info):
    clear_screen()
    header("DELETE ACCOUNT")
    space()
    warn_panel("PERMANENT DELETION WARNING \n\n"
    "By performing this action, you are permenently\n"
    "deleting your account. This action CANNOT be undone.\n\n"
    f"Account to be deleted:\n"
    f"- Name: {user_info['name']}\n"
    f"- Username: {user_info['username']}\n"
    f"- Email: {user_info['email']}\n",
    title="WARNING"
    )
    space()

    entered_password = get_input("Enter password to verify", password=True)

    if  not bcrypt.checkpw(entered_password.encode('utf-8'), user_info['password'].encode('utf-8')):
        space()
        error_panel("Incorrect password!\nDeletion cancelled for security.")
        sleep(2)
        return
    
    if bcrypt.checkpw(entered_password.encode('utf-8'), user_info['password'].encode('utf-8')):
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
    
    username = user_info['username']

    delete_user(username)

    success_panel(
        "Account Deleted Successfully!\n\n"
        f"User '{username} has been permanently removed.\n'"
        "Thank you for using our system."
        )
    space()

    end_session()

    status("Returning to main menu...", 2)

