from .validators import is_valid_email, is_unique_username, validate_password
from .ui import *
import time

def register_user(users, counter):
    clear_screen()
    header("Welcome to the Registration Page")
    space(2)
    #Name input
    
    first_name = get_input("Enter your First Name").title()
    space()
    last_name = get_input("Enter your Last Name").title()

    full_name = f"{first_name} {last_name}"

    #Email input
    while True:
        space()
        email = get_input("Enter Email id")
        if is_valid_email(email):
            break
        space()
        error("Invalid Email")

    #Username Creation
    while True:
        space()
        username = get_input("create Username").lower()
        if is_unique_username(username, users):
            break
        else:
            space()
            warn_panel("Username already taken")

    #Password Creation
    while True:
        space()
        password = get_input("Create a password")
    
        is_valid, message = validate_password(password, username)
        console.print(message)
        if is_valid:
            space()
            confirm = get_input("Confirm password")
            
            if password == confirm:
                space()
                break
            else:
                error("❌ Passwords don't match!")
        # else:
        #     warn()

#Storing in Dict
    user_id = f"u{counter:03d}"
    users[user_id] = {
        "Name" : full_name,
        "Email" : email,
        "Username" : username,
        "Password" : password
    }

    #Success message
    success_panel("Registration Successful!")
    sleep(1.6)

    return users, counter + 1