import random
print("Welcome to the game of Rock, Paper, Scissors\n")

rounds = int(input("How many rounds would you like to play: "))
player = 0
computer = 0
options = ["Rock", "Paper", "Scissors"]
for i in range(1, rounds+1):
    print("Round {}".format(i))
    print("Player: {}\tComputer: {}".format(player, computer))
    choice = input("Time to pick...Rock, Paper, Scissors: ").title()

    compChoice = random.randint(0, len(options)-1)
    print("\tComputer: {}".format(options[compChoice]))
    print("\tPlayer: {}".format(choice))

    if choice in options:
        if choice == options[compChoice]:
            print("\tIt is a tie, how boring!\n\tThis round was a tie.")
        elif choice == options[0] and options[compChoice] == options[2]:
            print("\tRock breaks Scissors!\n\tYou win round {}".format(i))
            player += 1
        elif choice == options[1] and options[compChoice] == options[0]:
            print("\tPaper covers Rock!\n\tYou win round {}".format(i))
            player += 1
        elif choice == options[2] and options[compChoice] == options[1]:
            print("\tScissors cut Paper!\n\tYou win round {}".format(i))
            player += 1
        elif choice == options[0] and options[compChoice] == options[1]:
            print("\tPaper covers Rock!\n\tComputer wins round {}".format(i))
            computer += 1
        elif choice == options[1] and options[compChoice] == options[2]:
            print("\tScissors cut Paper!\n\tComputer wins round {}".format(i))
            computer += 1
        elif choice == options[2] and options[compChoice] == options[0]:
            print("\tRock breaks Scissors!\n\tComputer wins round {}".format(i))
            computer += 1
    else:
        print("That is not a valid game option!\nComputer gets the point!")
        computer += 1
print()
print("Final Game Results")
print("\tRounds Played: {}".format(i))
print("\tPlayer Score: {}".format(player))
print("\tComputer Score: {}".format(computer))

if player > computer:
    print("\tWinner: Player :-)")
elif player == computer:
    print("\tIt is a tie :-/")
else:
    print("\tWinner: Computer :-(")