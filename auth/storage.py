import json

FILE = "data/user_data.json"
def load_users():
    try:
        with open(FILE) as f:
           return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent = 4)


