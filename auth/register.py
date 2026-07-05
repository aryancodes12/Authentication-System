from .validators import validate_password
from .ui import clear_screen, header, space, get_input, warn, error, success_panel, sleep, console
from database.insert import insert_user
from database.select import is_username_exists, is_email_exists

import time
import bcrypt

def register_user():
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
        if is_email_exists(email):
            space()
            warn("Email already registered. Try different Email")
            continue
        break

    #Username Creation
    while True:
        space()
        username = get_input("create Username").lower()

        if is_username_exists(username):
            space()
            warn("Username already taken. Try different username")
            continue
        break

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
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                space()

                break
            else:
                error("❌ Passwords don't match!")

# Storing in Database
    insert_values = [full_name, username, email, hashed_password.decode('utf-8')]
    insert_user(*insert_values)


    #Success message
    clear_screen()
    success_panel("Registration Successful!")
    sleep(1.6)