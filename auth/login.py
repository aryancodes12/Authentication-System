from .ui import console, panel, success, warn, error, status, rule
from .validators import is_username_exist, is_email_exist, is_pass_matched

def login(users):
    rule("Login Page")
    panel("Welcome to the Login Page")
    while True:
        console.print("\nEnter your username or email ('m' for Menu)")
        username = input(">>> ").lower()
        if username == "q":
            break
        if is_username_exist(username, users) or is_email_exist(username, users):
            while True:
                console.print("\nEnter password")
                password = input(">>> ")
                if is_pass_matched(password, users):
                    panel(f"Welcome back, {username}")
                    break
                else:
                    error("Incorrect password or username")
            break
        else:
            error("Username not found")
    return username

