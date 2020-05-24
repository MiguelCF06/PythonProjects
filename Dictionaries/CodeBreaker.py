from collections import Counter
print("Welcome to the Code Breaker App\n")

nonLetters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", ",", "?", "!", "'", '"', ":", ";", ")", "(",
              "[", "]", "+", "*", "-", "_", "=", "%", "#", "/", "|", "\n", "\t", "&"]


phrase = """
As McMurdo had said, the house in which he lived was a lonely one and very well
suited for such a crime as they had planned. It was on the extreme fringe of the town and stood well back from the road.
In any other case the conspirators would have simply called out their man, as they had many a time before, and emptied
their pistols into his body;
but in this instance it was very necessary to find out how much he knew, how he knew it, and what had been passed on to
his employers.
It was possible that they were already too late and that the work had been done.
If that was indeed so, they could at least have their revenge upon the man who had done it.
But they were hopeful that nothing of great importance had yet come to the detective's knowledge, as otherwise,
they argued, he would not have troubled to write down and forward such trivial information as McMurdo claimed to have
given him. However, all this they would learn from his own lips. Once in their power,
they would find a way to make him speak, z.
It was not the first time that they had handled an unwilling witness. 
"""
phrase = phrase.lower()
print()
for nonLetter in nonLetters:
    phrase = phrase.replace(nonLetter, "")

numberOfLetters = len(phrase)
countOfEachLetter = Counter(phrase)

print("Here is the frequency analysis from key phrase 1:\n")
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

phrase2 = """
When he had returned home he made his own preparations for the grim evening in front of him.
First he cleaned, oiled, and loaded his Smith & Wesson revolver.
Then he surveyed the room in which the detective was to be trapped.
It was a large apartment, with a long deal table in the centre, and the big stove at one side.
At each of the other sides were windows.
There were no shutters on these: only light curtains which drew across.
McMurdo examined these attentively, z.
No doubt it must have struck him that the apartment was very exposed for so secret a meeting.
Yet its distance from the road made it of less consequence.
Finally he discussed the matter with his fellow lodger.
Scanlan, though a Scowrer, was an inoffensive little man who was too weak to stand against the opinion of his comrades,
but was secretly horrified by the deeds of blood at which he had sometimes been forced to assist.
McMurdo told him shortly what was intended. 
"""
phrase2 = phrase2.lower()
print()
for nonLetter in nonLetters:
    phrase2 = phrase2.replace(nonLetter, "")

numberOfLetters = len(phrase2)
countOfEachLetter = Counter(phrase2)

print("Here is the frequency analysis from key phrase 2:\n")
print("\tLetter\t\tOcurrence\t\tPercentage")
for key, values in sorted(countOfEachLetter.items()):
    percentage = 100 * values/numberOfLetters
    print("\t{}\t\t{}\t\t\t{:.2f}".format(key, values, percentage))

orderedLetterCount = countOfEachLetter.most_common()
listOfOrderedLettersPhrase2 = []

for pair in orderedLetterCount:
    listOfOrderedLettersPhrase2.append(pair[0])
print("Letters ordered from highest ocurrence to lowest:")
for letter in listOfOrderedLettersPhrase2:
    print(letter, end="")
print()
print()
EncOrDec = input("Would you like to encode or decode a message: ").lower().strip()
code = input("What is the phrase: ").lower()

for nonLetter in nonLetters:
    code = code.replace(nonLetter, "")

if EncOrDec == "encode":
    encodedPhrase = []
    for letter in code:
        idx = listOfOrderedLetters.index(letter)
        changed = listOfOrderedLettersPhrase2[idx]
        encodedPhrase.append(changed)
    print("The encoded message is:")
    for lttr in encodedPhrase:
        print(lttr, end="")
elif EncOrDec == "decode":
    decodedPhrase = []
    for letter in code:
        idx = listOfOrderedLettersPhrase2.index(letter)
        changed = listOfOrderedLetters[idx]
        decodedPhrase.append(changed)
    print("The decoded phrase is:")
    for lttr in decodedPhrase:
        print(lttr, end="")
else:
    print("That is not a right option. Type 'encode' or 'decode'.")