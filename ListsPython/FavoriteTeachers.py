print("Welcome to the Favorite Teachers program")
print()

teachers = []

teachers.append(input("Who is your first favorite teacher: ").title())
teachers.append(input("Who is your second favorite teacher: ").title())
teachers.append(input("Who is your third favorite teacher: ").title())
teachers.append(input("Who is your fourth favorite teacher: ").title())
print()

print("Your favorite teachers ranked are: {}".format(teachers))
print("Your favorite teachers alphabetically are: {}".format(sorted(teachers)))
print("Your favorite teachers in reverse alphabetical order are: {}".format(sorted(teachers, reverse=True)))
print()


print("Your two top teachers are: {} and {}".format(teachers[0], teachers[1]))
print("Your next two favorite teachers are: {} and {}".format(teachers[2], teachers[3]))
print("Your last favorite teacher is: {}".format(teachers[-1]))
print("You have a total of {} favorite teachers.".format(len(teachers)))
print()

print("Oops, {} is no longer your first favorite teacher. ".format(teachers[0]), end="")
new = input("Who is your new FAVORITE teacher: ").title()
teachers.insert(0, new)

print("Your favorite teachers ranked are: {}".format(teachers))
print("Your favorite teachers alphabetically are: {}".format(sorted(teachers)))
print("Your favorite teachers in reverse alphabetical order are: {}".format(sorted(teachers, reverse=True)))
print()

print("Your two top teachers are: {} and {}".format(teachers[0], teachers[1]))
print("Your next two favorite teachers are: {} and {}".format(teachers[2], teachers[3]))
print("Your last favorite teacher is: {}".format(teachers[-1]))
print("You have a total of {} favorite teachers.".format(len(teachers)))
print()

print("You have decided you no longer like a teacher. ", end="")
teachers.remove(input("Which teacher would you like to remove from your list: ").title())
print()

print("Your favorite teachers ranked are: {}".format(teachers))
print("Your favorite teachers alphabetically are: {}".format(sorted(teachers)))
print("Your favorite teachers in reverse alphabetical order are: {}".format(sorted(teachers, reverse=True)))
print()

print("Your two top teachers are: {} and {}".format(teachers[0], teachers[1]))
print("Your next two favorite teachers are: {} and {}".format(teachers[2], teachers[3]))
print("Your last favorite teacher is: {}".format(teachers[-1]))
print("You have a total of {} favorite teachers.".format(len(teachers)))