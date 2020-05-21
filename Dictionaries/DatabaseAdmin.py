print("Welcome to the Database Admin Program\n")

usersInDatabase = {
    "loke123": "naught90",
    "kast902": "plk987jim",
    "plim456": "wert234nm",
    "lostin234": "findout567",
    "admin00": "admin123",
}

username = input("Enter your username: ")

if username in usersInDatabase.keys():
    password = input("Enter your password: ")
    print()
    if password in usersInDatabase[username]:
        print("Hello {}! You are logged in!".format(username))
        if username == "admin00":
            print("Here is the current user database:")
            for users, passwords in usersInDatabase.items():
                print("Username: {}\t\tPassword: {}".format(users, passwords))
        else:
            changePswd = input("Would you like to change your password (yes/no): ").lower()
            if changePswd == "yes":
                newPassword = input("What would you like your new password to be: ")
                print()
                if len(newPassword) < 8:
                    print("The password must be 8 characters or more long.")
                    print("Your password still be {}. Goodbye.".format(password))
                else:
                    password = newPassword
                    print("{} now your password is {}".format(username, password))
            else:
                print("Okay so goodbye!")
else:
    print("That user is not in the database. Goodbye")