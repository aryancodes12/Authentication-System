from .ui import *
from .sessions import end_session
from .storage import save_users

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
        sleep(1)
        space(2)
    elif choice == '1':
        # clear_screen()
        show_users(users)
        
    elif choice == "2":
        clear_screen()
        delete_user(users)
    elif choice == "3":
        clear_screen()
        search(users)
    elif choice == "4":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        space()
        warn("Invalid Choice")




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
    wait_for_enter("Press 'Enter' to go back")


#DELETE USERS
def delete_user(users):
    header("REGISTERED USERS")

    uid = get_input("Enter user's UID to delete or 'q' to quit")

    found = None
    if uid == 'q':
        return None
    elif uid != 'q':
        for id in users.keys():
            if uid == id:
                success_panel("UID Found in database")
                found = id
                break

    if not found:
        error_panel("UID not found in the database")
        status("Returning to menu ...", 1)
        return None

    if found:
        warn_panel("This action is cannot be undone.\n KEYWORD: DESTROY")
        keyword = "DESTROY"
        confirm = get_input("Enter KEYWORD to delete or 'q' to quit")

        if confirm == 'q':
            return None
        
        if confirm == keyword:
            del users[found]
            save_users(users)
            success_panel("User DESTROYED successfully.")
            
            status("Returing to menu...", 1)
        else:
            error_panel("Wrong 'KEYWORD' mission aborted")
            status("Returing to menu...",1)


def search(users):
    header("Search users")

    search = get_input("Enter Name/Email/Username to search user: ")
    user_list = []
    
    #for loop
    for user in users.values():
        name = user['Name']
        user_list.append(name)
    
    print(user_list)
    sleep(4)
    wait_for_enter()