print("Welcome to the Yes or No Issue Polling App\n")

adminPassword = "p0ll1ng"

surveyQuestion = input("What is the yes or no issue you will be voting on today: ")
numberOfVoters = int(input("What is the number of voters you will allow on the issue: "))

password = input("Enter a password for polling results: ")
print()
yes = 0
no = 0
results = {}
listOfNames = []
listOfChoices = []


if password == adminPassword:
    for i in range(numberOfVoters):
        name = input("Enter your full name: ").title()
        if name in results.keys():
            print("Sorry, it seems that someone with that name has already voted.")
        else:
            print("Here is our issue: {}".format(surveyQuestion))
            choice = input("What do you think...yes or no: ").lower()
            if choice == "yes":
                yes += 1
            elif choice == "no":
                no += 1
            else:
                print("That is not a yes or no answer, but okay...")
            print("Thank you {}! Your vote of {} has been recorded.".format(name, choice))
            print()
        listOfNames.append(name)
        listOfChoices.append(choice)
        results = dict(zip(listOfNames, listOfChoices))
    print("The following {} people voted:".format(len(listOfNames)))
    for name in listOfNames:
        print(name)
    print()
    print("On the following issue: {}".format(surveyQuestion))
    if yes == no:
        print("It was a tie! {} votes to {}.".format(yes, no))
    if yes > no:
        print("Yes won! {} votes to {}.".format(yes, no))
    if yes < no:
        print("No won! {} votes to {}.".format(no, yes))
    print()
    pswdAgain = input("To see the voting results enter the admin password: ")
    if pswdAgain == adminPassword:
        for keys, values in results.items():
            print("Voter: {}\t\tVote: {}".format(keys, values))
        print()
    else:
        print("Oops, it seems that you forgot the password, Goodbye.")
    print("Thank you for using the Yes or No Issue Polling App.")
else:
    print("You're not the admin. Goodbye.")