import bcrypt
from .ui import clear_screen, header, space, get_input, warn_panel, error_panel, success_panel, status
from database.select import is_username_exists, is_correct_pass

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