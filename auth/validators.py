def is_valid_email(email):
    return "@gmail.com" in email

def is_unique_username(username, users):
    return username not in [u["Username"] for u in users.values()]

    

