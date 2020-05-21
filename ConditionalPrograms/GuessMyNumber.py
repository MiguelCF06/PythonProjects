from random import randint

Intentos = 1

print("HELLO THIS IS THE GUESSER GAME\n")

MinNum = 1
MaxNum = int(input("Enter the range of numbers that you want to guess: "))
playerLifes = int(input("Enter the amount of lives that you want (Less than 11): ")) - 1

if playerLifes > 10:
    while playerLifes > 10:
            playerLifes = int(input("Enter a number LESS THAN 11!: ")) - 1
elif playerLifes == 0:
    while playerLifes == 0:
        playerLifes = int(input("Enter a valid life more than 1: ")) - 1

print("You have only {} lifes for guess the number\n".format(playerLifes + 1))

randNum = randint(MinNum, MaxNum)
player = int(input("Enter a number between 1 and {}: ".format(MaxNum)))

while playerLifes != 0:
    if player == randNum:
        print("YOU WON, you guess the number in {} tries!".format(Intentos))
        break
    elif player + 1 == randNum or player - 1 == randNum:
        print("Your number is within 1 of the number\n")
        player = int(input("Enter the number: "))
        Intentos = Intentos + 1
        playerLifes = playerLifes - 1
    elif player < randNum:
        player = int(input("Enter a higher number: "))
        Intentos = Intentos + 1
        playerLifes = playerLifes - 1
    elif player > randNum:
        player = int(input("Enter a lower number: "))
        Intentos = Intentos + 1
        playerLifes = playerLifes - 1
if playerLifes == 0:
    print("You lose all your lifes :(\n")
    print("The number was: {}\n".format(randNum))

