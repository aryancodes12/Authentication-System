from .validators import is_valid_email, is_unique_username
from .ui import console, success, warn, error

def register_user(users, counter):
    console.print("Enter your First Name", style = "cyan")
    first_name = input(">>> ").title()
    console.print("\nEnter your Last Name", style = "cyan")
    last_name = input(">>> ").title()

    full_name = f"{first_name} {last_name}"

    while True:
        console.print("\nEnter Email Id", style = "cyan")
        email = input(">>> ")
        if is_valid_email(email):
            break
        error("Invalid Email")

    while True:
        console.print("\nCreate Username", style = "cyan")
        username = input(">>> ").lower()
        if is_unique_username(username, users):
            break
        else:
            warn("Username already taken")

    while True:
        console.print("\nCreate a password", style = "cyan")
        password = input(">>> ")
        if password == username:
            warn("Password cannot match Username")
        elif len(password) < 8:
            warn("Password must be of 8 character or more")
        else:
            console.print("\nConfirm the password" , style = "cyan")
            confirm = input(">>> ")
            break

    user_id = f"u{counter:03d}"
    users[user_id] = {
        "Name" : full_name,
        "Email" : email,
        "Username" : username,
        "Password" : password
    }

    success("Registration Successful!")

    return users, counter + 1
