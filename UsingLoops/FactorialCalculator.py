import math
print("Welcome to the Factorial Calculator App\n")

number = int(input("What number would you like to compute the factorial of: "))

print("{}! = ".format(number), end="")
for x in range(1, number):
	print("{}".format(x), end="*")
print("{}\n".format(number))

print("Here is the result from the math library:")

factorial1 = math.factorial(number)

print("The factorial of {} is {}!\n".format(number, factorial1))

print("Here is the result from my own algorithm:")

factorial2 = 1
for x in range(1, number+1):
	factorial2 = factorial2 * x
print("The factorial of {} is {}!\n".format(number, factorial2))

print("It is shown twice that {}! = {} (with excitement)".format(number, factorial1))