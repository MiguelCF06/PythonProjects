print("Welcome to the Fibonacci Calculator App\n")

amount = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
print()

fib = [1, 1]
for x in range(amount-2):
	alg = fib[x] + fib[x+1]
	fib.append(alg)

print("The first {} numbers of the Fibonacci sequence are:".format(amount))
for num in fib:
	print(num)
print()

print("The corresponding Golden Ratio values are:")

gratio = [fib[i] / float(fib[i-1]) for i in range(1,len(fib))]

for num in gratio:
	print(num)
print()

print("The ratio of consecutive Fibonacci terms approaches Phi; {:.3f}...".format(gratio[-1]))