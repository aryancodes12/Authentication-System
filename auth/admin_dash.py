from .ui import *
from .sessions import end_session
import bcrypt
from database.select import select_all_users, is_username_exists, is_correct_pass, select_users_by_name
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

    elif choice == '1':
        clear_screen()
        show_users()


    elif choice == "2":
        clear_screen()
        delete_user_with_username()
    elif choice == "3":
        clear_screen()
        search()

    elif choice == "4":
        end_session()
        status("\nLogging Out ...", 1)
        status("\nReturning to Main Menu ...", 1)
    else:
        space()
        warn("Invalid Choice")


def show_users():
    clear_screen()
    status("Loading information...", 0.4)
    header("REGISTERED USERS")
    data = select_all_users()
    console.print(display_user_table(data))
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


def search():
    while True:
        clear_screen()
        header("SEARCH USERS")
        query = get_input("Search user by Name").strip()

        results = select_users_by_name(query)
        
        if results:
            success_panel(f"Names containing '{query}' found in the database")

            table = Table(style=HEADER)

            table.add_column("User Id", style = SUCCESS)
            table.add_column("Name", style = ACCENT)
            table.add_column("Username", style = WARNING)
            table.add_column("Email", style = PRIMARY)

            for result in results:
                table.add_row(
                    str(result['id']),
                    result["name"],
                    result["username"],
                    result["email"]
                    )
            console.print(table)
            choice = get_input("Search again? (y/n)").lower()
            if choice == 'y':
                continue
            elif choice == 'n':
                break
            else:
                warn_panel("Invalid choice, returning to menu...")
                status("Returing to the menu... ", 1)
                    
        else:
            warn_panel("User not found")
            sleep(4)
            status("Returing to the menu... ", 0.5)