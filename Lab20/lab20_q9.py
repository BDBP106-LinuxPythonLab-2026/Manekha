while True:
    password = input("Enter a password: ")
    errors = []

    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch in "!@#$%&*":
            special = True

    if not upper:
        errors.append("Password must contain an uppercase letter.")

    if not lower:
        errors.append("Password must contain a lowercase letter.")

    if not digit:
        errors.append("Password must contain a digit.")

    if not special:
        errors.append("Password must contain a special character.")

    if " " in password:
        errors.append("Password must not contain spaces.")

    if "password" in password.lower():
        errors.append("Password must not contain the word 'password'.")

    if len(errors) == 0:
        print("Password accepted!")
        break
    else:
        print("Invalid password. Problems:")
        for error in errors:
            print("-", error)