print("Welcome to the Voter Registration App\n")

parties = ["Republican", "Democratic", "Independent", "Green"]

name = input("Please enter your name: ").title()
age = int(input("Please enter your age: "))
print()
if age < 18:
    print("You're not old enough to register to vote")
else:
    print("Congratulations {}! You are old enough to register to vote\n".format(name))

    print("Here is a list of political parties to join.")
    for party in parties:
        print("\t- {}".format(party))
    print()
    choice = input("What party would you like to join: ").title()
    print()
    if choice in parties:
        print("Congratulations {}! You have joined the {} party!".format(name, choice))

        if choice == parties[0]:
            print("That is a major party!")
        elif choice == parties[1]:
            print("That is a major party!")
        elif choice == parties[2]:
            print("That is not a major party!")
        elif choice == parties[3]:
            print("That is not a major party!")
    else:
        print("Invalid option")