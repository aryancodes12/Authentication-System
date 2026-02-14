def is_valid_email(email):
    return "@gmail.com" in email

def is_unique_username(username, users):
    return username not in [u["Username"] for u in users.values()]

def validate_password(password, username):
    if not password:
        return False, "Password cannot be empty"

    if password == username:
        return False, "⚠️ Password cannot match username"
    
    if len(password) < 8:
        return False, "⚠️ Password must be at least 8 characters"
    
    # Check for special characters
    special_chars = "@_!#$%^&*"
    if not any(char in special_chars for char in password):
        return False, f"⚠️ Password must include a special character ({special_chars})"
    
    # Check for at least one number
    if not any(char.isdigit() for char in password):
        return False, "⚠️ Password must include at least one number"
    
    return True, "✓ Password is valid"