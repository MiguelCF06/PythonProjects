print("Welcome to the Binary/Hexadecimal Converter App\n")

decimal = []
binary = []
hexadecimal = []

amount = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists... Complete\n")

for number in range(1, amount + 1):
	decimal.append(number)
	binary.append(bin(number))
	hexadecimal.append(hex(number))

print("Using slices, we will now show a portion of each list.")

begin = int(input("What decimal number would you like to start at: "))
end = int(input("What decimal number would you like to stop at: "))

print("Decimal values from {} to {}:".format(begin, end))
for num in range(begin-1, end):
	print(decimal[num])
print()

print("Binary values from {} to {}:".format(begin, end))
for num in range(begin-1, end):
	print(binary[num])
print()

print("Hexadecimal values from {} to {}:".format(begin, end))
for num in range(begin-1, end):
	print(hexadecimal[num])
print()

input("Press Enter to see all values from 1 to {}.".format(amount))

print("Decimal--------------Binary--------------Hexadecimal")
print("--------------------------------------------------")
for num in range(len(decimal)):
	print("{}-------------------{}-----------------{}".format(decimal[num], binary[num], hexadecimal[num]))
