print("Welcome to the Temperature Conversion Program")
print()
Fahr = float(input("What is the given temperature in degrees Fahrenheit: "))
kelvin = (Fahr-32)*5/9 + 273.15
celsius = (Fahr-32)*5/9

print("Degrees Fahrenheit:\t{:.4f}".format(Fahr))
print("Degrees Celsius:\t{:.4f}".format(celsius))
print("Degrees Kelvin:\t{:.4f}".format(kelvin))