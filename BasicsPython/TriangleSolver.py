import math
print("Welcome to the Right Triangle Solver App")
print()
leg1 = float(input("What is the first leg of the triangle: "))
leg2 = float(input("What is the second leg of the triangle: "))
print()
hypotenuse = math.sqrt(leg1**2 + leg2**2)
area = 1/2 * leg1 * leg2
print("For a triangle with legs of {} and {} the hypotenuse is {:.3f}".format(leg1, leg2, hypotenuse))
print("For a triangle with legs of {} and {} the area is {:.3f}".format(leg1, leg2, area))