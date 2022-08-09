from donation_pkg.homepage import show_homepage, donate, show_donations
from donation_pkg.user import login, register


database = {"admin": "123"}
donations = []
authorized_user = ""


while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")

    else:
        print("Logged in as:", authorized_user)

    choice = input("Choose an option: ")
    print("\n")

# Login
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

# Register
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username, password)

        if authorized_user != "":
            database[username] = password

# Donate
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in.")

        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)


# Show Donations
    elif choice == "4":
        show_donations(donations)

# Exit
    elif choice == "5":
        print("Goodbye")
        exit()
    print("\n")
