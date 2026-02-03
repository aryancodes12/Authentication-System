def is_valid_email(email):
    return "@" in email and "." in email

def is_unique_username(username, users):
    return username not in [u["Username"] for u in users.values()]
