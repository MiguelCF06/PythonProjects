print("Welcome to the Average Calculator App\n")

name = input("What is your name: ").title()
amount = int(input("How many grades would you like to enter: "))

gradesList = []

for i in range(amount):
	grades = int(input("Enter grade: "))
	gradesList.append(grades)
print()

print("Grades Highest to Lowest:")

average = 0

gradesList.sort(reverse=True)
for grade in gradesList:
	print(grade)
	average += grade
print()

average = average / len(gradesList)

print("{}'s Grade Summary:".format(name))
print("\t\tTotal Number of Grades: {}".format(amount))
print("\t\tHighest Grade: {}".format(gradesList[0]))
print("\t\tLowest Grade: {}".format(gradesList[-1]))
print("\t\tAverage: {:.2f}\n".format(average))

desiredAverage = int(input("What is your desired average: "))
print()

newGrade = desiredAverage * (len(gradesList)+1) - sum(gradesList)

print("Good Luck {}!".format(name))
print("You'll need to get a {} on your next assignment to earn a {} average".format(newGrade, desiredAverage))
print()

print("Lets see what your average could have been if you did better/worse on an assignment")

copyList = gradesList[:]

remvGrade = int(input("What grade would you like to change: "))

copyList.remove(remvGrade)

changeGrade = int(input("What grade would you like to change {} to: ".format(remvGrade)))
copyList.append(changeGrade)
print()

print("New grades Highest to Lowest:")

copyList.sort(reverse=True)

for num in copyList:
	print(num)
print()

avg2 = sum(copyList) / len(copyList)

print("{}'s New Grade Summary:".format(name))
print("\t\tTotal Number of Grades: {}".format(amount))
print("\t\tHighest Grade: {}".format(copyList[0]))
print("\t\tLowest Grade: {}".format(copyList[-1]))
print("\t\tAverage: {:.2f}\n".format(avg2))
print()

print("Your new average would be a {} compared to your real average of {}".format(avg2, average))

difference = avg2 - average

print("That is a change of {:.2f} points!".format(difference))
print()

print("Too bad your original grades are still the same!")
print(gradesList)
print("You should ask for extra credit!")