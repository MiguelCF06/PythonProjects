from collections import Counter
print("Welcome to the Frequency Analysis App\n")

nonLetters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", ",", "?", "!", "'", '"', ":", ";", ")", "(",
              "[", "]", "+", "*", "-", "_", "=", "%", "#", "/", "|"]


for i in range(1, 3):
    phrase = input("Enter a word or phrase to count the ocurrence of each letter: ")
    print()
    for nonLetter in nonLetters:
        phrase = phrase.replace(nonLetter, "")

    numberOfLetters = len(phrase)
    countOfEachLetter = Counter(phrase)

    print("Here is the frequency analysis from key phrase {}:\n".format(i))
    print("\tLetter\t\tOcurrence\t\tPercentage")
    for key, values in sorted(countOfEachLetter.items()):
        percentage = 100 * values/numberOfLetters
        print("\t{}\t\t{}\t\t\t{:.2f}".format(key, values, percentage))

    orderedLetterCount = countOfEachLetter.most_common()
    listOfOrderedLetters = []

    for pair in orderedLetterCount:
        listOfOrderedLetters.append(pair[0])
    print("Letters ordered from highest ocurrence to lowest:")
    for letter in listOfOrderedLetters:
        print(letter, end="")
    print()