import cmath
print("Welcome to the Quadratic Solver App\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

amount = int(input("How many equations would you like to solve today: "))
print()

for x in range(amount):
	print("Solving equation #{}".format(x+1))
	print("----------------------------------\n")

	a = float(input("Please enter your value of a (coefficient of x^2): "))
	b = float(input("Please enter your value of b (coefficient of x): "))
	c = float(input("Please enter your value of c (coefficient): "))
	print()
	
	d = (b**2) - (4*a*c)

	sol1 = (-b+cmath.sqrt(d))/(2*a)
	sol2 = (-b-cmath.sqrt(d))/(2*a)

	print("The solutions of {}x^2 + {}x + {} are:\n".format(a, b, c))
	
	print("\t\tx1 = {}".format(sol1))
	print("\t\tx2 = {}".format(sol2))
	print()

print("Thank you for using the Quadratic Equation Solver App.  Goodbye.")