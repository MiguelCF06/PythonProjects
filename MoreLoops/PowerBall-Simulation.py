import random
print("----------------------Power-Ball Simulator----------------------\n")

whiteBalls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if whiteBalls < 5:
    whiteBalls = 5
redBalls = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))
if redBalls < 1:
    redBalls = 1

odds = 1

for i in range(5):
    odds *= whiteBalls - 1
odds *= redBalls / 120

print("You have a 1 in {:.1f} chance of winning this lottery".format(odds))

interval = int(input("Purchase tickets in what interval: "))
print()

winning = []
while len(winning) < 5:
    ranNum = random.randint(1, whiteBalls)
    if ranNum not in winning:
        winning.append(ranNum)
winning.sort()

numberRed = random.randint(1, redBalls)
winning.append(numberRed)

print("-------------Welcome to the Power-Ball-------------\n")
print("Tonight's winning numbers are: ", end="")
for num in winning:
    print(str(num), end=" ")
print()
input("Press 'Enter' to begin purchasing tickets!!!\n")

purchased = 0
playing = True
sold = []

while winning not in sold and playing:
    lottery = []
    while len(lottery) < 5:
        number = random.randint(1, whiteBalls)
        if number not in lottery:
            lottery.append(number)
    lottery.sort()

    numberRedBalls = random.randint(1, redBalls)
    lottery.append(numberRedBalls)

    if lottery not in sold:
        purchased += 1
        sold.append(lottery)
        print(lottery)
    else:
        print("Losing ticket generated: disregard...")

    if purchased % interval == 0:
        print("{} tickets purchased so far with no winners...\n".format(purchased))
        ans = input("Keep purchasing tickets (y/n): ").lower().strip()
        if ans != "y":
            playing = False

if lottery == winning:
    print("Winning ticket numbers: ", end="")
    for number in lottery:
        print(str(number),end=" ")
    print("\nPurchased a total of {} tickets.".format(purchased))
else:
    print("\nYou bought {} tickets and still lost!".format(purchased))
    print("Better luck next time!")