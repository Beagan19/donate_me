def login(database, username, password):
    username = username.lower()
    if len(username) > 10:
        print("Username cannot be over 10 characters.")
    if len(password) < 5:
        print("Password must be at least 5 characters.")
    if username in database:
        if password == database[username]:
            print("Welcome,", username)
            return username
        print("Incorrect password.")
        return ""
    print("User not found. Please register.")
    return ""


def register(database, username, password):
    username = username.lower()
    if len(username) > 10:
        print("Username cannot be over 10 characters.")
    if len(password) < 5:
        print("Password must be at least 5 characters.")

    if username in database:
        print("Username already registered.")
        return ""
    print("Username has been registered.")
    return username
