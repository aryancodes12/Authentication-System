from .ui import *
import bcrypt

def login(users):
    clear_screen()
    header("Welcome to LOGIN page")
    space()

    #Username / Email input
    while True:
        username = get_input("Enter Username or Email ('q' to quit)")


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
            wait_for_enter()
            return None

        #Password input
        attempts = 3
        while attempts > 0:
            space()
            warn_panel(f"{attempts} attempts left")
            entered_Password = get_input("Password", password=True)

            if bcrypt.checkpw(entered_Password.encode('utf-8'), user["Password"].encode('utf-8')):

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
                    status("Returning to main menu...", 0.5)
                    return None