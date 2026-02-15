from .ui import *

def login(users):
    clear_screen()
    header("LOGIN", "Welcome back!")
    space()

    #Username / Email input
    while True:
        # console.print("\nEnter your username or email ('q' to quit)", style="cyan")
        username = get_input("Username or Email")


        if username == "q":
            return None

        user = None
        for u in users.values():
            if u["Username"].lower() == username or u["Email"] == username:
                user = u
                break
        if not user:
            error("User not Found")
            wait_for_enter()
            return None

        #Password input
        attempts = 3
        while attempts > 0:
            console.print(f"\n([yellow]{attempts} attempts left[/yellow])", style="cyan")
            password = get_input("Password", password=True)

            if password == user["Password"]:
                success_panel(f"Welcome back, {user['Name']}!")
                status("Starting session...", 1)
                return user
            else:
                attempts -= 1
                if attempts > 0:
                    error(f"Incorrect password! {attempts} attempts remaining")
                else:
                    error_panel("Too many failed attempts")
                    warn_panel("Returning to main menu..")
                    status("", 1)
                    return None