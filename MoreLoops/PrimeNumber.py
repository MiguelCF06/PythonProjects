import time
print("Welcome to the Prime Number App\n")

flag = True

while flag:
    print("Enter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = int(input("Enter your choice 1 or 2: "))
    print()
    if choice == 1:
        number = int(input("Enter a number for determine if it is prime or not: "))
        for i in range(2, number):
            if number % i == 0:
                print("{} is not prime!\n".format(number))
                break
        else:
            print("{} is prime!".format(number))
    elif choice == 2:
        minRange = int(input("Enter the lower bound of your range: "))
        maxRange = int(input("Enter the upper bound of your range: "))

        evenNum = []
        start_time = time.time()
        for num in range(minRange, maxRange):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    evenNum.append(num)
        print("Calculations took a total of {:.4f}".format(time.time()-start_time))
        print("The following numbers between {} to {} are prime:".format(minRange, maxRange))
        input("Press enter to continue.")
        for num in evenNum:
            print(num)
    print()

    ans = input("Would you like to run the program again (y/n) : ").lower().strip()

    if ans != "y":
        flag = False