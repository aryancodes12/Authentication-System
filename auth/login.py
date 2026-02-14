from .ui import *

def login(users):
    clear_screen()
    rule("")
    panel("Welcome to Login Page")

    #Username / Email input
    while True:
        console.print("\nEnter your username or email ('q' to quit)", style="cyan")
        identifier = input(">>> ").strip().lower()

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

        #Password input
        attempts = 3
        while attempts > 0:
            console.print(f"\nEnter Password ([yellow]{attempts} attempts left[/yellow])", style="cyan")
            password = input(">>> ")

            if password == user["Password"]:
                panel(f"Welcome back, {user['Name']}!")
                status("Starting session...", 1)
                return user
            else:
                attempts -= 1
                if attempts > 0:
                    error(f"Incorrect password! {attempts} attempts remaining")
                else:
                    error("Too many failed attempts")
                    warn("Returning to main menu..")
                    status("", 1)
                    return None