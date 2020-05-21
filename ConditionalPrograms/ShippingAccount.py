print("Welcome to the Shipping Accounts Program\n")

username = ["mikeL", "Omar293", "JJlk", "JoelW"]

user = input("Hello, what is your username: ")

if user not in username:
	print("Sorry, you do not have an account with us. Goodbye.")
else:
	print("Hello {}. Welcome back to your account.".format(user))
	print("Current shipping prices are as follows:\n")

	print("Shipping orders 0 to 100:\t\t$5.10 each")
	print("Shipping orders 100 to 500:\t\t$5.00 each")
	print("Shipping orders 500 to 1000:\t$4.95 each")
	print("Shipping orders over 1000:\t\t$4.80 each\n")

	amount = int(input("How many items would you like to ship: "))


	if amount <= 0:
		print("Nothing to do.")
	if amount > 0 and amount <= 100:
		items = 5.10
		price = items * amount
		print("To ship {} items it will cost you ${} at $5.10 per item.".format(amount, price))
	elif amount > 100 and amount <= 500:
		items = 5.00
		price = items * amount
		print("To ship {} items it will cost you ${} at $5.00 per item.".format(amount, price))
	elif amount > 500 and amount <= 1000:
		items = 4.95
		price = items * amount
		print("To ship {} items it will cost you ${} at $4.95 per item.".format(amount, price))
	else:
		items = 4.80
		price = items * amount
		print("To ship {} items it will cost you ${} at $4.80 per item.".format(amount, price))
	print()
	answer = input("Would you like to place this order (y/n): ")

	if answer == "n" or answer == "N":
		print("Okay, no order is being placed at this time.")
	elif answer == "y" or answer == "Y":
		print("Okay. Shipping your {} items.".format(amount))