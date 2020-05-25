import random

def dice(sides, rolls):
    ranNum = random.randint(0, sides)
    return ranNum

print("Welcome to the Python Dice App\n")

flag = True

while flag:
    sides = int(input("How many sides would you like on your dice: "))
    rolls = int(input("How many dice would you like to roll: "))
    total = 0
    result = []

    print("You rolled {} times a {} sided dice.\n".format(rolls, sides))
    print("-----Results are as followed-----")
    for times in range(rolls):
        result.append(dice(sides, rolls))
    for num in result:
        total += num
        print("\t", num)
    print("The total value of your roll is {}".format(total))
    print()

    ans = input("Would you like to roll again (y/n): ").lower().strip()
    print()
    if ans != "y":
        print("Thank you for using the Python Dice App.")
        flag = False