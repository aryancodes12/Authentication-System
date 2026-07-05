from .ui import clear_screen, header, space, get_input, warn_panel, error_panel, success_panel, status
import bcrypt
from database.select import is_username_exists, is_correct_pass

#Main login function
def login():
    clear_screen()
    header("Welcome to LOGIN page")
    space()

    #Username / Email input
    while True:
        username = get_input("Enter Username or Email ('q' to quit)")

        if username == "q":
            return None

        user = None
        
        if is_username_exists(username):
            user = username

        if not is_username_exists(username):
            space()
            error_panel("User not Found")
            continue
            # return None

        #Password input
        attempts = 3
        while attempts > 0:
            space()
            warn_panel(f"{attempts} attempts left")
            entered_password = get_input("Password", password=True)

            user_pass = is_correct_pass(user)

            if bcrypt.checkpw(entered_password.encode('utf-8'), user_pass['password'].encode('utf-8')):
                space(2)
                success_panel(f"Welcome back, {user}!")
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
                    status("Returning to main menu...", 0.5)
                    return None