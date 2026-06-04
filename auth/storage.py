import json
import bcrypt

FILE = "user_data.json"

def load_users():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent = 4)

def admin_data(users):
    password = "admin321"
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    admin_data = {
        'Name' : 'Admin',
        'Email' : 'admin@system.com',
        'Username': 'admin',
        'Password' : hashed_pw.decode('utf-8')
    }

    users['A000'] = admin_data
    save_users(users)