import re

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter"

    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter"

    if not re.search(r"[0-9]", password):
        return False, "Password must contain a number"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain a special character"

    if " " in password:
        return False, "Password must not contain spaces"

    return True, "Password is valid"

if __name__ == "__main__":
    password = input("Enter a password: ")
    valid, message = validate_password(password)
    print(message)

