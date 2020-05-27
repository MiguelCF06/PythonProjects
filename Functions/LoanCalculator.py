from matplotlib import pyplot
def setLoan():
    loanAmount = float(input("Enter the loan amount: "))
    interest = float(input("Enter the interest rate: "))/100
    monthlyPayment = float(input("Enter the desired monthly payment amount: "))

    loanInfo = {
        "Principal": loanAmount,
        "Rate": interest,
        "Monthly Payment": monthlyPayment,
        "Money Paid": 0,
    }
    return loanInfo

def showInfo(loanInfo, iter):
    print("\n-----Loan information after {} months.-----".format(iter))
    for key, value in loanInfo.items():
        print("{}: {:.3f}".format(key, value))
    print()

def interestAm(loan):
    loan["Principal"] = loan["Principal"] + loan["Principal"] * loan["Rate"]/12

def makePayment(loan):
    loan["Principal"] -= loan["Monthly Payment"]
    if loan["Principal"] > 0:
        loan["Money Paid"] += loan["Monthly Payment"]
    else:
        loan["Money Paid"] += loan["Monthly Payment"] + loan["Principal"]
        loan["Principal"] = 0

def summary(loan, months, initialLoan):
    print("Congratulations! You paid off your loan in {} months!".format(months))
    print("Your initial loan was ${:.2f} at a rate of {:.2f}%".format(initialLoan, loan["Rate"]*100))
    print("Your monthly payment was ${:.2f}.".format(loan["Monthly Payment"]))
    print("You spent ${:.2f} in total.".format(loan["Money Paid"]))
    interest = loan["Money Paid"] - initialLoan
    print("You spent ${:.2f}".format(interest))
def createGraph(data, loan):
    xValues = []
    yValues = []
    for point in data:
        xValues.append(point[0])
        yValues.append(point[1])
    pyplot.plot(xValues, yValues)
    pyplot.title("{}% Interest With {} Monthly Payment".format(loan["Rate"]*100, loan["Monthly Payment"]))
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()

print("Welcome to the Loan Calculator App\n")
myLoan = setLoan()
months = 0
initialLoan = myLoan["Principal"]
showInfo(myLoan, months)
dataPlot = []

input("Press 'Enter' to begin paying off your loan.")
while myLoan["Principal"] > 0:
    if myLoan["Principal"] > initialLoan:
        break
    months += 1
    interestAm(myLoan)
    makePayment(myLoan)
    dataPlot.append((months, myLoan["Principal"]))
    showInfo(myLoan, months)
if myLoan["Principal"] <= 0:
    summary(myLoan, months, initialLoan)
    createGraph(dataPlot, myLoan)
else:
    print("\nYou will NEVER pay off your loan!!!")
    print("You cannot get ahead of the interest! :-(")