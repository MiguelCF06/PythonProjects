print("Welcome to the Letter Counter App")
print()
name = input("What is your name: ")
print("Hello {}!".format(name))
print("I'm going to count the number of times that a specific letter occurs in a message")
print()

msg = input("Please enter a message: ")
msg = msg.lower()
counter = input("Which letter would you like to count the ocurrences of: ")
ocurrences = msg.count(counter)

print("{}, your message has {} {}'s in it".format(name, ocurrences, counter))