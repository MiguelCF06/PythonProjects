import random
print("Welcome to the Guess My Word App\n")

categories = {
    "Sports":["soccer", "football", "tennis", "baseball", "basketball"],
    "Fruits":["apple", "pineapple", "grape", "watermelon", "strawberry"],
    "Games":["zelda", "uncharted", "resident evil", "god of war", "the last of us"],
    "Series":["stranger things", "money heist", "dark", "elite", "house of flowers"]
}

flag = True

while flag:
    guesses = 1
    flag2 = True
    randomCategory, randomValue = random.choice(list(categories.items()))
    ranIdx = random.randint(0, len(randomValue) - 1)
    word = randomValue[ranIdx]
    lines = []
    for letter in word:
        lines.append("-")
    print("Guess a letter word from the following category: {}".format(randomCategory))
    while flag2:
        print("".join(lines))

        guess = input("Enter your guess: ").lower()
        print()

        if guess == word:
            print("Correct! You guessed the word in {} guesses".format(guesses))
            print()
            flag2 = False
        elif guess != word:
            print("That is not correct. Let us reveal a letter to help you!")
            guesses += 1
            swap = True
            while swap:
                idx = random.randint(0, len(word)-1)
                if lines[idx] == "-":
                    lines[idx] = word[idx]
                    swap = False

    ans = input("Would you like to play again (y/n): ").lower().strip()
    print()
    if ans != "y":
        flag = False
print("Thank you for playing the game!")