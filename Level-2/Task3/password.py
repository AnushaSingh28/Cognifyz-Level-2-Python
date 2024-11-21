# Create a Python function that evaluates the strength of a password entered by the user. Implement checks for factors such as length, presence of uppercase andlowercase letters, digits, and special characters.
def check_password_strength(password):
    
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        return

    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter.")
        return

    if not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter.")
        return

    if not any(char.isdigit() for char in password):
        print("Password should have at least one number.")
        return

    special_characters = "!@#$%^&*()-_+=<>?/"
    if not any(char in special_characters for char in password):
        print("Password should have at least one special character.")
        return

    # If all checks pass
    print("Password is strong!")

password = input("Enter your password: ")
check_password_strength(password)
