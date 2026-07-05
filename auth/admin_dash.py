from .ui import *
from .sessions import end_session
import bcrypt
from database.select import select_all_users, is_username_exists, is_correct_pass
from database.delete import delete_user

def admin_dash():
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
        clear_screen()
        show_users()


    elif choice == "2":
        clear_screen()
        delete_user_with_username()
    elif choice == "3":
        clear_screen()
        header("Search and Filter users")

        # query = get_input("Search user by Name/Email/Username/UID ").strip()

        # results = search(users, query)
        
        
        
        # if results:
        #     success_panel(f"Result found {len(results)} user(s)\n")

        #     table = Table(style=HEADER)

        #     table.add_column("User Id", style = SUCCESS)
        #     table.add_column("Name", style = ACCENT)
        #     table.add_column("Email", style = WARNING)
        #     table.add_column("Username", style = PRIMARY)

        #     for uid, info in results:
        #         table.add_row(
        #         uid,
        #         info["Name"],
        #         info["Email"],
        #         info["Username"]
        #         )
        #     console.print(table)
        #     wait_for_enter()
        #     status("Returing to the menu... ", 0.5)
        # else:
        #     print()
        #     warn_panel("User not found")
        #     sleep(4)
        #     status("Returing to the menu... ", 0.5)


    elif choice == "4":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        space()
        warn("Invalid Choice")




def admin_login():
    clear_screen()
    header("ADMIN LOGIN page")
    space()

    #Username
    while True:
        username = get_input("Enter Admin Username  ('q' to quit)")


        if username == "q":
            return None

        admin = None

        if is_username_exists(username):
            admin = username

        if not is_username_exists(username):
            space()
            error_panel("Wrong Credentials")
            continue

        #Password input
        attempts = 3
        while attempts > 0:
            space()
            warn_panel(f"{attempts} attempts left")
            entered_password = get_input("Password", password=True)

            admin_pass = is_correct_pass(admin)
            if bcrypt.checkpw(entered_password.encode('utf-8'), admin_pass['password'].encode('utf-8')):
                space(2)
                success_panel(f"Welcome back, {admin}!")
                space()
                status("Starting session...", 1)
                return admin
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

def show_users():
    clear_screen()
    status("Loading information...", 0.4)
    header("REGISTERED USERS")
    data = select_all_users()
    console.print(display_user_table(data, title="Registered Users"))
    space()
    wait_for_enter("Press 'Enter' to go back")


#DELETE USERS
def delete_user_with_username():
    header("REGISTERED USERS")

    username = get_input("Enter user's username to delete or 'q' to quit")

    found = None
    if username == 'q':
        return None
    
    found = is_username_exists(username)

    if not found:
        error_panel("Username not found in the database")
        status("Returning to menu ...", 1)
        return None

    if found:
        warn_panel("This action is cannot be undone.\n KEYWORD: DESTROY")
        keyword = "DESTROY"
        confirm = get_input("Enter KEYWORD to delete or 'q' to quit")

        if confirm == 'q':
            return None
        
        if confirm == keyword:
            delete_user(username)
            success_panel("User DESTROYED successfully.")
            
            status("Returing to menu...", 1)
        else:
            error_panel("Wrong 'KEYWORD' mission aborted")
            status("Returing to menu...",1)


def search(users, query):
    result = []
    query = query.lower().strip()

    for uid, data in users.items():
        if (query in data['Name'].lower() or
            query in data['Email'].lower() or
            query in data["Username"].lower() or
            query == uid.lower()):
            result.append((uid, data))

    return result