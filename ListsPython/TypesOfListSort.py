print("\t\t\tSummary Table")
print()
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.14256]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("The variable num_strings is a {}.".format(type(num_strings)))
print("It contains the elements: {}".format(num_strings))
print("The element {} is a {}.".format(num_strings[0], type(num_strings[0])))
print()

print("The variable num_ints is a {}.".format(type(num_ints)))
print("It contains the elements: {}".format(num_ints))
print("The element {} is a {}.".format(num_ints[0], type(num_ints[0])))
print()

print("The variable num_floats is a {}.".format(type(num_floats)))
print("It contains the elements: {}".format(num_floats))
print("The element {} is a {}.".format(num_floats[0], type(num_floats[0])))
print()

print("The variable num_lists is a {}.".format(type(num_lists)))
print("It contains the elements: {}".format(num_lists))
print("The element {} is a {}.".format(num_lists[0], type(num_lists[0])))
print()

num_strings.sort()
num_ints.sort()

print("Now sorting num_strings and num_ints...")
print("Sorted num_strings: {}".format(num_strings))
print("Sorted num_ints: {}".format(num_ints))
print()
print("Strings are sorted alphabetically while integers are sorted numerically!")