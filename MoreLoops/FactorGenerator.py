print("Welcome to the Factor Generator App\n")

flag = True

while flag:
    factors = []
    number = int(input("Enter a number to determine all factors of that number: "))
    print()
    print("The factors of {} are:".format(number))
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    for factor in factors:
        print(factor)
    print()
    print("In summary:")
    for i in range(int(len(factors)/2)):
        print("{} * {} = {}".format(factors[i], factors[-i-1], number))
    print()
    answer = input("Run again? (y/n): ").lower()
    if answer != "y":
        flag = False
print("Thank you for using the program. Have a great day.")