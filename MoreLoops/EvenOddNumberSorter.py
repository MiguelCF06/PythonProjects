print("Welcome to the Even Odd Number Sorter App\n")

flag = True

while flag:
    numbers = input("Enter in a string of numbers separated by a comma (,) : ")
    numbers = numbers.replace(" ", "")
    numList = numbers.split(",")
    print()
    even = []
    odd = []

    print("---- Result Summary ----")
    for number in numList:
        number = int(number)
        if number % 2 == 0:
            even.append(number)
            print("\t{} is even!".format(number))
        else:
            odd.append(number)
            print("\t{} is odd!".format(number))
    print()

    print("The following {} numbers are even:".format(len(even)))
    for num in even:
        print("\t{}".format(num))
    print()

    print("The following {} numbers are odd:".format(len(odd)))
    for num in odd:
        print("\t{}".format(num))
    print()

    ans = input("Would you like to run the program again? (y/n): ").lower().strip()
    print()
    if ans != "y":
        flag = False