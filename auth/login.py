import os
from .ui import console, panel, success, warn, error, status, rule, page

def login(users):
    rule("Login Page")
    panel("Welcome to Login Page")

    while True:
        console.print("\nEnter your username or email ('q' to quit)")
        identifier = input(">>> ").lower()

        if identifier == "q":
            return None

        user = None
        for u in users.values():
            if u["Username"].lower() == identifier or u["Email"] == identifier:
                user = u
                break
        if not user:
            error("User not Found")
            continue
        for i in range(3, 0, -1):
            console.print("\nEnter password")
            password = input(">>> ")

            if password == user["Password"]:
                panel(f"Welcome back, {user['Name']}", "green")
                return user
            else:
                error("Incorrect Password")
                i -= 1
                if i == 0:
                    break
