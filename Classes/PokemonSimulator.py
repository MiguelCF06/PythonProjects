import random


class Pokemon():
    def __init__(self, name, type, health, speed):
        self.name = name.title()
        self.type = type
        self.health = health
        self.maxHealth = health
        self.speed = speed
        self.isAlive = True

    def lightAttack(self, enemyPok):
        damage = random.randint(15, 25)
        print("{} use {}.".format(self.name, self.moves[0]))
        print("The attack dealt {} of damage.\n".format(damage))
        enemyPok.health -= damage

    def heavyAttack(self, enemyPok):
        damage = random.randint(0, 50)
        print("{} use {}.".format(self.name, self.moves[1]))
        if damage < 10:
            print("The attack missed\n")
        else:
            print("The attack dealt {} of damage.\n".format(damage))
            enemyPok.health -= damage

    def restore(self):
        heal = random.randint(15, 25)
        print("{} use {}".format(self.name, self.moves[2]))
        print("{} has restored {} ps\n".format(self.name, heal))
        self.health += heal
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def faint(self):
        if self.health <= 0:
            self.isAlive = False
            print("\n{} has fainted.\n".format(self.name))
            input("\nPress 'enter' to continue...")

    def showStats(self):
        print("Name: {}".format(self.name))
        print("Type: {}".format(self.type))
        print("Current Health: {}".format(self.health))
        print("Max health: {}".format(self.maxHealth))
        print("Speed: {}".format(self.speed))


class Fire(Pokemon):
    def __init__(self, name, type, health, speed):
        super().__init__(name, type, health, speed)
        self.moves = ["Scratch", "Ember", "Light", "Fire Blast"]

    def specialAttack(self, enemyPok):
        print("{} used {}!".format(self.name, self.moves[3]))
        if enemyPok.type is "GRASS":
            print("Was super effective!!!")
            damage = random.randint(40, 60)
        elif enemyPok.type is "WATER":
            print("Is not very effective.")
            damage = random.randint(0, 5)
        else:
            damage = random.randint(15, 30)
        print("It deals {} damage!\n".format(damage))
        enemyPok.health -= damage

    def moveInfo(self):
        print("\n{} moves.".format(self.name))
        # Light Attack
        print("--- {} ---".format(self.moves[0]))
        print("An efficient attack.")
        print("Deals a damage within a range of 15 to 25 points.")
        # Heavy Attack
        print("--- {} ---".format(self.moves[1]))
        print("A risky attack...")
        print("Could deal damage up to 50 damage points or fail and deal 0 points")
        # Restore move
        print("--- {} ---".format(self.moves[2]))
        print("A restorative move...")
        print("Heal your pokemon from 15 to 25 points")
        # Special Attack
        print("--- {} ---".format(self.moves[3]))
        print("A powerful FIRE based attack!")
        print("Guaranteed to deal MASSIVE damage to GRASS type Pokemon.\n")


class Water(Pokemon):
    def __init__(self, name, type, health, speed):
        super().__init__(name, type, health, speed)
        self.moves = ["Bite", "Splash", "Dive", "Water Cannon"]

    def specialAttack(self, enemyPok):
        print("{} used {}!".format(self.name, self.moves[3]))
        if enemyPok.type is "FIRE":
            print("Was super effective!!!")
            damage = random.randint(40, 60)
        elif enemyPok.type is "GRASS":
            print("Is not very effective.")
            damage = random.randint(0, 5)
        else:
            damage = random.randint(15, 30)
        print("It deals {} damage!\n".format(damage))
        enemyPok.health -= damage

    def moveInfo(self):
        print("\n{} moves.".format(self.name))
        # Light Attack
        print("--- {} ---".format(self.moves[0]))
        print("An efficient attack.")
        print("Deals a damage within a range of 15 to 25 points.")
        # Heavy Attack
        print("--- {} ---".format(self.moves[1]))
        print("A risky attack...")
        print("Could deal damage up to 50 damage points or fail and deal 0 points")
        # Restore move
        print("--- {} ---".format(self.moves[2]))
        print("A restorative move...")
        print("Heal your pokemon from 15 to 25 points")
        # Special Attack
        print("--- {} ---".format(self.moves[3]))
        print("A powerful WATER based attack!")
        print("Guaranteed to deal MASSIVE damage to FIRE type Pokemon.\n")


class Grass(Pokemon):
    def __init__(self, name, type, health, speed):
        super().__init__(name, type, health, speed)
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]

    def specialAttack(self, enemyPok):
        print("{} used {}!".format(self.name, self.moves[3]))
        if enemyPok.type is "WATER":
            print("Was super effective!!!")
            damage = random.randint(40, 60)
        elif enemyPok.type is "FIRE":
            print("Is not very effective.")
            damage = random.randint(0, 5)
        else:
            damage = random.randint(15, 30)
        print("It deals {} damage!\n".format(damage))
        enemyPok.health -= damage

    def moveInfo(self):
        print("\n{} moves.".format(self.name))
        # Light Attack
        print("--- {} ---".format(self.moves[0]))
        print("An efficient attack.")
        print("Deals a damage within a range of 15 to 25 points.")
        # Heavy Attack
        print("--- {} ---".format(self.moves[1]))
        print("A risky attack...")
        print("Could deal damage up to 50 damage points or fail and deal 0 points")
        # Restore move
        print("--- {} ---".format(self.moves[2]))
        print("A restorative move...")
        print("Heal your pokemon from 15 to 25 points")
        # Special Attack
        print("--- {} ---".format(self.moves[3]))
        print("A powerful GRASS based attack!")
        print("Guaranteed to deal MASSIVE damage to WATER type Pokemon.\n")


class Game():
    def __init__(self):
        self.pokemonTypes = ["FIRE", "WATER", "GRASS"]
        self.pokemonNames = ["Hyely", "Dinonite", "Koalith", "Tiguzz", "Steelvark", "Whirlnea", "Oddaroo",
                             "Burnosaur", "Potatoad", "Quaileaf", "Wallastar", "Turtou", "Quickerine", "Spidia"]
        self.battlesWon = 0

    def createPokemon(self):
        health = random.randint(70, 100)
        speed = random.randint(1, 10)
        type = random.choice(self.pokemonTypes)
        name = random.choice(self.pokemonNames)
        if type == "FIRE":
            pokemon = Fire(name, type, health, speed)
        elif type == "WATER":
            pokemon = Water(name, type, health, speed)
        else:
            pokemon = Grass(name, type, health, speed)
        return pokemon

    def choosePokemon(self):
        starters = []
        while len(starters) < 3:
            pokemon = self.createPokemon()
            validPokemon = True
            for starter in starters:
                if starter.name == pokemon.name or starter.type == pokemon.type:
                    validPokemon = False
            if validPokemon:
                starters.append(pokemon)

        for starter in starters:
            starter.showStats()
            starter.moveInfo()

        print("\nProfessor Oak presents you with three Pokemon: ")
        print("(1) - {}".format(starters[0].name))
        print("(2) - {}".format(starters[1].name))
        print("(3) - {}".format(starters[2].name))
        choice = int(input("Which Pokemon do you want to choose: "))
        pokemon = starters[choice - 1]
        return pokemon

    def getAttack(self, pokemon):
        print("\nWhat move would you like to do?")
        print("Press 1 for {}.".format(pokemon.moves[0]))
        print("Press 2 for {}.".format(pokemon.moves[1]))
        print("Press 3 for {}".format(pokemon.moves[2]))
        print("Press 4 for {}".format(pokemon.moves[3]))
        choice = int(input("Please enter your move choice: "))
        print()
        print("------------------------------------------------------------------")
        return choice

    def playerAttack(self, move, player, computer):
        if move == 1:
            player.lightAttack(computer)
        elif move == 2:
            player.heavyAttack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.specialAttack(computer)
        computer.faint()

    def computerAttack(self, player, computer):
        move = random.randint(1, 4)
        if move == 1:
            computer.lightAttack(player)
        elif move == 2:
            computer.heavyAttack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.specialAttack(player)
        player.faint()

    def battle(self, player, computer):
        move = self.getAttack(player)
        if player.speed >= computer.speed:
            self.playerAttack(move, player, computer)
            if computer.isAlive:
                self.computerAttack(player, computer)
        else:
            self.computerAttack(player, computer)
            if player.isAlive:
                self.playerAttack(move, player, computer)


print("Welcome to Pokemon!")
print("Can you become the World's greatest Pokemon Trainer???\n")

print("Don't worry! Prof Oak is here to help you on your quest.")
print("He would like to gift you your first Pokemon")
print("Here are three potential Pokemon Partners.")
input("Press 'enter' to choose your Pokemon\n")

playing = True
while playing:
    game = Game()

    player = game.choosePokemon()
    print("\nCongratulations Trainer, you have chosen {}!".format(player.name))
    input("\nYour journey with {} begins now... Press Enter!".format(player.name))

    while player.isAlive:
        computer = game.createPokemon()
        print("Oh no! a wild {} has approached!".format(computer.name))
        computer.showStats()

        while computer.isAlive and player.isAlive:
            game.battle(player, computer)
            if computer.isAlive and player.isAlive:
                player.showStats()
                computer.showStats()
        if player.isAlive:
            game.battlesWon += 1

    print("Poor {} has fainted".format(player.name))
    print("But not before defeating {} Pokemons!".format(game.battlesWon))

    again = input("Would you like to play again? (y/n): ").lower()
    if again != "y":
        playing = False
        print("Thank you for playing Pokemon!")