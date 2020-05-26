def setAccount():
    print("Welcome to the Python First National Bank\n")
    name = input("Hello, what is your name: ").title()
    savings = int(input("How much money would you like to set up your savings account with: "))
    checking = int(input("How much money would you like to set up your checking account with: "))
    print()

    account = {
        "Name": name,
        "Savings": savings,
        "Checking": checking,
    }
    return account

def deposits(account, type, money):
    account[type] += money
    print("Deposited ${} into {}'s {} account.\n".format(money, account["Name"], type))
def withdrawals(account, type, money):
    if account[type] - money < 0:
        print("Sorry, by withdrawing ${} you will have a negative balance.".format(money))
    else:
        account[type] -= money
        print("Withdrew ${} into {}'s {} account.\n".format(money, account["Name"], type))

def showInfo(account):
    print("Current Account Information")
    for key, values in account.items():
        if isinstance(values, int):
            print("{}: ${}".format(key, values))
        else:
            print("{}: {}".format(key, values))

my_account = setAccount()
running = True
while running:
    showInfo(my_account)

    typeAcc = input("What account would you like to access (Savings or Checking): ").title().strip()
    typeTr = input("What type of transaction would you like to make (Deposit or withdrawal): ").lower().strip()
    money = int(input("How much money: "))
    print()
    if typeAcc == "Savings" or typeAcc == "Checking":
        if typeTr == "deposit":
            deposits(my_account, typeAcc, money)
        elif typeTr == "withdrawal":
            withdrawals(my_account, typeAcc, money)
        else:
            print("Invalid option.")
    else:
        print("That is not a valid option.")
    ans = input("Would you like to make another transaction (y/n): ").lower().strip()
    print()
    if ans != "y":
        showInfo(my_account)
        print("Thank you. Have a great day.")
        running = False