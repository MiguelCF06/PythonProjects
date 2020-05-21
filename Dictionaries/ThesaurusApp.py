import random
print("Welcome to the Thesaurus App\n")

thesaurus = {
    "Hot": ["balmy", "summery", "tropical", "boiling", "scorching"],
    "Cold": ["chilly", "cool", "freezing", "frigid", "polar"],
    "Happy": ["content", "cheery", "merry", "jovial", "jocular"],
    "Sad": ["unhappy", "downcast", "miserable", "glum", "melancholy"],
}

print("Choose a word from the Thesaurus and I will give you a synonym.\n")

print("Here are the words in the Thesaurus:")
for key in thesaurus.keys():
    print("-{}".format(key))
print()

choice = input("What word would you like a synonym for: ").title()

randomNum = random.randint(0, 4)

for key, values in thesaurus.items():
    if choice in key:
        print("A synonym for {} is {}.".format(choice, values[randomNum]))
        break
    else:
        print("That word is not in the Thesaurus, sorry.")
        break
print()

answer = input("Would you like to see the whole thesaurus (yes/no): ").title()
print()
if answer == "Yes":
    for key, values in thesaurus.items():
        print("{} synonyms are: ".format(key))
        for value in values:
            print("\t- {}".format(value))
else:
    print("I hope you enjoyed the program.  Thank you!")