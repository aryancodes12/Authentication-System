from .ui import *

def login(users):
    clear_screen()
    rule("")
    panel("Welcome to Login Page")

    #Username / Email input
    while True:
        console.print("\nEnter your username or email ('q' to quit)", style="cyan")
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

        #Password input
        for i in range(3, 0, -1):
            console.print("\nEnter password", style="cyan")
            password = input(">>> ")

            if password == user["Password"]:
                return user
            else:
                error("Incorrect Password")
                i -= 1
                if i == 0:
                    break