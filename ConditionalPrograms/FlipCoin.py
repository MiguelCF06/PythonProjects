import random

print("Welcome to the Coin Toss App\n")

print("I will flip a coin a set number of times.")
flipTimes = int(input("How many times would you like me to flip the coin: "))
answer = input("Would you like to see the result of each flip (y/n): ")
print()
heads = 0
tails = 0

if answer == "y" or answer == "Y":
	print("Flipping!!!\n")
	for num in range(1, flipTimes):
		ranNumber = random.randint(0, 1)
		if ranNumber == 0:
			print("HEAD")
			heads += 1
		elif ranNumber == 1:
			print("TAIL")
			tails += 1
		if heads == tails:
			print("At {} flips, the number of heads and tails were equal at {} each.".format(num, heads))
			continue
	print()

	percentageH = heads * 100/flipTimes
	percentageT = tails * 100/flipTimes

	print("Results of flipping A coin {} times\n".format(flipTimes))
	print("Side\t\tCount\t\tPercentage")
	print("Heads\t\t{}/{}\t\t{:.2f}%".format(heads, flipTimes, percentageH))
	print("Tails\t\t{}/{}\t\t{:.2f}%".format(tails, flipTimes, percentageT))
else:
	print("Ok Goodbye...")