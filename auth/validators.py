def is_valid_email(email):
    return "@gmail.com" in email

def is_unique_username(username, users):
    return username not in [u["Username"] for u in users.values()]

def is_username_exist(username, users):
    return username in [u["Username"] for u in users.values()]

def is_email_exist(username, users):
    return username in [e["Email"] for e in users.values()]

def is_pass_matched(password, users):
    return password in [p["Password"] for p in users.values()]