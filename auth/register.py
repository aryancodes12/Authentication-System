from .validators import is_valid_email, is_unique_username, validate_password
from .ui import *
import time

def register_user(users, counter):
    clear_screen()
    rule("")
    panel("Welcome to the Registration Page")

    #Name input
    console.print("Enter your First Name", style = "cyan")
    first_name = input(">>> ").title()
    console.print("\nEnter your Last Name", style = "cyan")
    last_name = input(">>> ").title()

    full_name = f"{first_name} {last_name}"

    #Email input
    while True:
        console.print("\nEnter Email Id", style = "cyan")
        email = input(">>> ")
        if is_valid_email(email):
            break
        error("Invalid Email")

    #Username Creation
    while True:
        console.print("\nCreate Username", style = "cyan")
        username = input(">>> ").lower()
        if is_unique_username(username, users):
            break
        else:
            warn("Username already taken")

    #Password Creation
    while True:
        console.print("\nCreate a password", style="cyan")
        password = input(">>> ")
    
        is_valid, message = validate_password(password, username)
    
        if is_valid:
            console.print("\nConfirm the password", style="cyan")
            confirm = input(">>> ")
        
            if password == confirm:
                break
            else:
                error("❌ Passwords don't match!")
        else:
            warn(message)

#Storing in Dict
    user_id = f"u{counter:03d}"
    users[user_id] = {
        "Name" : full_name,
        "Email" : email,
        "Username" : username,
        "Password" : password
    }

    #Success message
    success("Registration Successful!")
    time.sleep(0.8)

    return users, counter + 1