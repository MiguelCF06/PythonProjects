def add(a, b):
    print("The sum of {:.1f} and {:.1f} is {:.1f}".format(a, b, a + b))
    return "{} + {} = {:.2f}".format(a, b, a+b)

def sub(a, b):
    print("The sub of {:.1f} and {:.1f} is {:.1f}".format(a, b, a - b))
    return "{} - {} = {:.2f}".format(a, b, a-b)

def mul(a, b):
    print("The mul of {:.1f} and {:.1f} is {:.1f}".format(a, b, a * b))
    return "{} * {} = {:.2f}".format(a, b, a*b)

def div(a, b):
    if a == 0 or b == 0:
        print("Can't divide by zero")
        return "DIV ZERO"
    print("The div of {:.1f} and {:.1f} is {:.1f}".format(a, b, a / b))
    return "{} / {} = {:.2f}".format(a, b, a/b)

def exp(a, b):
    print("The exp of {:.1f} and {:.1f} is {:.1f}".format(a, b, a ** b))
    return "{} ^ {} = {:.2f}".format(a, b, a**b)

def selectOperation(history):
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    op = input("Enter an operation (add, sub, mul, div, exp): ")
    if op == "add":
        x = add(a, b)
        history.append(x)
    elif op == "sub":
        x = sub(a, b)
        history.append(x)
    elif op == "mul":
        x = mul(a, b)
        history.append(x)
    elif op == "div":
        x = div(a, b)
        history.append(x)
    elif op == "exp":
        x = exp(a, b)
        history.append(x)
    else:
        print("That is not a valid operation. Try again.")
        history.append("OPP ERROR")
    return history

print("Welcome to the Python Calculator App")
print("Enter two numbers and an operation to be calculated.")
print()

running = True
history = []

while running:
    selectOperation(history)
    ans = input("Would you like to run the program again (y/n): ").lower().strip()
    if ans != "y":
        running = False
print("\nCalculation Summary:")
for oper in history:
    print(oper)