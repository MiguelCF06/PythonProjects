print("Welcome to the Basketball Rooster Program")
print()

roster = []

roster.append(input("Who is your point guard: ").title())
roster.append(input("Who is your shooting guard: ").title())
roster.append(input("Who is your small forward: ").title())
roster.append(input("Who is your power forward: ").title())
roster.append(input("Who is your center: ").title())
print()

print("\t\tYour starting 5 for the upcoming basketball season")
print("\t\t\t\tPoint Guard:\t\t\t{}".format(roster[0]))
print("\t\t\t\tShooting Guard:\t\t\t{}".format(roster[1]))
print("\t\t\t\tSmall Forward:\t\t\t{}".format(roster[2]))
print("\t\t\t\tPower Forward:\t\t\t{}".format(roster[3]))
print("\t\t\t\tCenter:\t\t\t\t\t{}".format(roster[4]))
print()

print("Oh no, {} is injured.".format(roster[3]))
print("Your roster only has 4 players")
roster[3] = input("Who will take {}'s spot: ".format(roster[3]).title())
print()

print("\t\tYour starting 5 for the upcoming basketball season")
print("\t\t\t\tPoint Guard:\t\t\t{}".format(roster[0]))
print("\t\t\t\tShooting Guard:\t\t\t{}".format(roster[1]))
print("\t\t\t\tSmall Forward:\t\t\t{}".format(roster[2]))
print("\t\t\t\tPower Forward:\t\t\t{}".format(roster[3]))
print("\t\t\t\tCenter:\t\t\t\t\t{}".format(roster[4]))
print()

print("Good luck {} you will do great!".format(roster[3]))
print("Your roster now has 5 players.")