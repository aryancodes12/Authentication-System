import json
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


# ===============================
# 👤 USER CLASS (single user)
# ===============================
class User:
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    # convert object → dict (for JSON saving)
    def to_dict(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Username": self.username,
            "Password": self.password
        }


# ===============================
# 🧠 SYSTEM CLASS (whole app)
# ===============================
class UserSystem:

    # -------- INIT (data owner) --------
    def __init__(self):
        self.users = {}
        self.counter = 1
        self.file_name = "user_data.json"
        self.load_data()


    # -------- LOAD DATA --------
    def load_data(self):
        try:
            with open(self.file_name) as f:
                raw = json.load(f)

            for uid, info in raw.items():
                self.users[uid] = User(
                    info["Name"],
                    info["Email"],
                    info["Username"],
                    info["Password"]
                )

            if self.users:
                self.counter = max(int(uid[1:]) for uid in self.users) + 1

            with console.status("Loading previous Data....", spinner="moon"):
                time.sleep(1)

        except FileNotFoundError:
            pass


    # -------- SAVE DATA --------
    def save_data(self):
        data = {uid: user.to_dict() for uid, user in self.users.items()}

        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

        with console.status("Saving Data ....", spinner="moon"):
            time.sleep(1)

        console.print("Data Saved", style="bold green")


    # -------- VALIDATIONS --------
    def is_valid_email(self, email):
        return "@" in email and "." in email

    def is_unique_username(self, username):
        return username not in [u.username for u in self.users.values()]


    # -------- REGISTER USER --------
    def register_user(self):

        console.print("Enter First Name", style="cyan")
        first = input(">>> ").title()

        console.print("\nEnter Last Name", style="cyan")
        last = input(">>> ").title()

        full_name = f"{first} {last}"

        # email
        while True:
            console.print("\nEnter Email", style="cyan")
            email = input(">>> ")
            if self.is_valid_email(email):
                break
            console.print("Invalid email", style="red")

        # username
        while True:
            console.print("\nCreate Username", style="cyan")
            username = input(">>> ")
            if self.is_unique_username(username):
                break
            console.print("Username taken", style="yellow")

        # password
        while True:
            console.print("\nCreate Password", style="cyan")
            password = input(">>> ")

            if len(password) < 8:
                console.print("Min 8 characters", style="red")
                continue

            console.print("\nConfirm Password", style="cyan")
            confirm = input(">>> ")

            if password == confirm:
                break

        # create object
        user = User(full_name, email, username, password)

        uid = f"u{self.counter:03d}"
        self.users[uid] = user
        self.counter += 1

        console.print("Registration Successful!", style="bold green")


    # -------- DISPLAY TABLE --------
    def display_users(self):
        table = Table(title="Registered Users")

        table.add_column("User ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Email", style="yellow")
        table.add_column("Username", style="magenta")

        for uid, user in self.users.items():
            table.add_row(uid, user.name, user.email, user.username)

        console.print(table)


    # -------- MAIN LOOP --------
    def run(self):

        while True:
            os.system("clear")  # change to clear for linux

            console.rule("[bold blue]Main Menu")
            console.print(Panel("👤 User Registration System"))

            console.print("1. Register User")
            console.print("2. Exit")

            choice = input(">>> ")

            if choice == "1":
                self.register_user()

            elif choice == "2":
                self.save_data()
                self.display_users()
                break

            else:
                console.print("Invalid choice", style="yellow")


# ===============================
# 🚀 ENTRY POINT
# ===============================
if __name__ == "__main__":
    app = UserSystem()
    app.run()
