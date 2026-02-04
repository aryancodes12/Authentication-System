 
from .ui import console, panel, success, warn, error, status, rule
from .validators import is_username_exist, is_pass_matched

def login(users):
    panel("Welcome to the Login Page")
    while True:
        console.print("\nEnter your username or email")
        username = input(">>> ").lower()
        if is_username_exist(username, users):
            success("Username exist")
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



