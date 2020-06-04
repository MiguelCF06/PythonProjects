import random

class Creature():
    """The pythonagachi creature class"""
        def __init__(self, name):
            """Initialize the attributes of the creature"""
            self.name = name
            self.hunger = 0
            self.boredom = 0
            self.tiredness = 0
            self.dirtiness = 0
            self.food = 2
            self.is_sleeping = False
            self.is_alive = True

        def eat(self):
            """Method for creature eats"""
            if self.food != 0:
                self.food -= 1
                ranNum = random.randint(1, 4)
                self.hunger -= ranNum
                print("\n{} ate a very great meal!".format(self.name))
            else:
                print("\n{} has no food!".format(self.name))
            if self.hunger <= 0:
                self.hunger = 0

        def play(self):
            """Method for play with the creature"""
            print("\n{} wants to play a game!".format(self.name))
            creatureNum = random.randint(0, 2)
            print("{} is thinking of a number 0, 1 or 2".format(self.name))
            userNum = int(input("Choose a number: "))
            if userNum == creatureNum:
                print("That's correct!, you won!")
                self.boredom -= 3
            else:
                print("That's not correct! :(")
                self.boredom -= 1
            if self.boredom <= 0:
                self.boredom = 0

        def sleep(self):
            """Method for the creature to go to sleep"""
            self.is_sleeping = True
            self.tiredness -= 3
            self.boredom -= 2
            print("{} is sleeping zzZ!".format(self.name))
            if self.tiredness <= 0:
                self.tiredness = 0
            if self.boredom <= 0:
                self.boredom = 0

        def awake(self):
            """Method for awake the creature"""
            ranNum = random.randint(0, 2)
            if ranNum == 0:
                print("{} just woke up!".format(self.name))
                self.is_sleeping = False
                self.boredom = 0
            else:
                print("{} won't wake up! :/".format(self.name))
                self.sleep()

        def clean(self):
            """Method for clean the creature"""
            self.dirtiness = 0
            print("{} has took a bath!".format(self.name))

        def forage(self):
            """Method for going for food"""
            foodFound = random.randint(0, 4)
            self.food += foodFound
            self.dirtiness += 2
            print("{} has found {} pieces of food".format(self.name, foodFound))

        def showValues(self):
            """Method that shows the attributes of the creature"""
            print("Creature Name: {}".format(self.name))
            print("Hunger (0-10): {}".format(self.hunger))
            print("Boredom (0-10): {}".format(self.boredom))
            print("Tiredness (0-10): {}".format(self.tiredness))
            print("Dirtinees (0-10): {}".format(self.dirtiness))
            print("\nFood inventory: {} pieces".format(self.food))
            if self.is_sleeping == True:
                print("Current Status: Sleeping")
            else:
                print("Current Status: Awake")

        def incrementValues(self, difficulty):
            """Method for increment each attributes conditioned
            by the difficulty"""
            ranNum = random.randint(0, difficulty)
            self.hunger += ranNum
            if self.is_sleeping == False:
                self.boredom += ranNum
                self.tiredness += ranNum
            self.dirtiness += ranNum

        def kill(self):
            """Method for look if the conditions kill the creature"""
            if self.hunger >= 10:
                print("{} starved to death! :(".format(self.name))
                self.is_alive = False
            elif self.dirtiness >= 10:
                print("{} suffered an infection and dies".format(self.name))
                self.is_alive = False
            elif self.boredom >= 10:
                self.boredom = 10
                print("{} is bored and falling sleep".format(self.name))
                self.is_sleeping = True
            elif self.tiredness >= 10:
                self.tiredness = 10
                print("{} is sleepy and falling asleep".format(self.name))
                self.is_sleeping = True

def showMenu(creature):
    if creature.is_sleeping == True:
        choice = int(input("\nEnter (6) to try and wake up: "))
        choice = 6
    else:
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
        choice = int(input("What is your choice: "))
    return choice

def callAction(creature, choice):
    if choice == 1:
        creature.eat()
    elif choice == 2:
        creature.play()
    elif choice == 3:
        creature.sleep()
    elif choice == 4:
        creature.clean()
    elif choice == 5:
        creature.forage()
    elif choice == 6:
        creature.awake()
    else:
        print("\nThat is not a valid option! Try again.")

print("Welcome to the Pythonagachi Simulator App")
difficulty = int(input("Please choose a difficulty level (1-5): "))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1
running = True

while running:
    nameCreature = input("What name would you like to give to your pet Pythonagachi: ").title()
    print()
    player = Creature(nameCreature)
    rounds = 1
    while player.is_alive:
        print("\nRound #{}".format(rounds))
        player.showValues()
        choice = showMenu(player)
        callAction(player, choice)
        print("\nRound #{} Summary:".format(rounds))
        player.showValues()
        input("Press Enter to continue...")
        player.incrementValues(difficulty)
        player.kill()
        rounds += 1
    print("{} R.I.P".format(nameCreature))
    print("Your creature survive {} rounds!".format(rounds))
    again = input("Would you like to play again? (y/n): ").lower()
    if again != "y":
        running = False
        print("Thanks for playing!!!")
