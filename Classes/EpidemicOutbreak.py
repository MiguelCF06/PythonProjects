import random


class Simulation:
    def __init__(self):
        self.dayNumber = 1

        print("To simulate an epidemic outbreak, we must know population size.")
        self.population = int(input("---Enter the population size: "))
        print()

        print("We must first start by infecting a portion of population.")
        self.percentInfected = float(input("---Enter the percentage (0-100) of the population to initially infect: "))
        print()
        self.percentInfected /= 100

        print("We must know the risk a person has to contract the disease when exposed.")
        self.probabilityInfect = float(input("---Enter the probability (0-100) that a person gets infected when exposed \
to the disease: "))
        print()

        print("We must know how long the infection will last when exposed.")
        self.days = int(input("---Enter the duration (in days) of the infection: "))
        print()

        print("We must know the mortality rate of those infected.")
        self.mortality = float(input("---Enter the mortality rate (0-100) of the infection: "))
        print()

        print("We must know how long to run the simulation.")
        self.daysToSimulate = int(input("---Enter the number of days to simulate: "))
        print()


class Person:
    def __init__(self):
        self.isInfected = False
        self.isDead = False
        self.daysInfected = 0

    def infect(self, simObj):
        chanceToBeInfected = random.randint(0, 100)
        if chanceToBeInfected < simObj.probabilityInfect:
            self.isInfected = True

    def heal(self):
        self.isInfected = False
        self.daysInfected = 0

    def die(self):
        self.isDead = True

    def update(self, simObj):
        if not self.isDead:
            if self.isInfected:
                self.daysInfected += 1
                mortalityRate = random.randint(0, 100)
                if mortalityRate < simObj.mortality:
                    self.die()
                elif self.daysInfected == simObj.days:
                    self.heal()


class Population:
    def __init__(self, simObj):
        self.population = []
        self.totalDeaths = 0
        for person in range(simObj.population):
            person = Person()
            self.population.append(person)

    def initialInfection(self, simObj):
        infectedCount = int(round(simObj.percentInfected * simObj.population, 0))
        for i in range(infectedCount):
            self.population[i].isInfected = True
            self.population[i].daysInfected = 1
        random.shuffle(self.population)

    def spread_infection(self, simObj):
        for x in range(len(self.population)):
            if not self.population[x].isDead:
                if x == 0:
                    if self.population[x + 1].isInfected:
                        self.population[x].infect(simObj)
                elif x < len(self.population) - 1:
                    if self.population[x + 1].isInfected or self.population[x - 1].isInfected:
                        self.population[x].infect(simObj)
                elif x == len(self.population) - 1:
                    if self.population[x - 1].isInfected:
                        self.population[x].infect(simObj)

    def update(self, simObj):
        simObj.dayNumber += 1
        for person in self.population:
            person.update(simObj)

    def displayStatistics(self, simObj):
        totalInfectedCount = 0
        self.totalDeaths = 0
        for person in self.population:
            if person.isInfected:
                totalInfectedCount += 1
                if person.isDead:
                    self.totalDeaths += 1
        infectedPercent = round(100 * (totalInfectedCount / simObj.population), 4)
        deathPercent = round(100 * (self.totalDeaths / simObj.population), 4)
        print("\n-----Day #{}-----".format(simObj.dayNumber))
        print("Percentage of Population Infected: {}%".format(infectedPercent))
        print("Percentage of Population Dead: {}%".format(deathPercent))
        print("Total People Infected: {} / {}".format(totalInfectedCount, simObj.population))
        print("Total Deaths: {} / {}".format(self.totalDeaths, simObj.population))

    def graphics(self):
        status = []
        for person in self.population:
            if person.isDead:
                char = "X"
            else:
                if person.isInfected:
                    char = "I"
                else:
                    char = "O"
            status.append(char)
        for letter in status:
            print(letter, end="-")


simulation = Simulation()
population = Population(simulation)

population.initialInfection(simulation)
population.displayStatistics(simulation)
population.graphics()
input("\nPress enter to begin the simulation...")

for x in range(1, simulation.daysToSimulate):
    population.spread_infection(simulation)
    population.update(simulation)
    population.displayStatistics(simulation)
    population.graphics()
    if population.totalDeaths == simulation.population:
        print("\nAll the {} humans was exterminated in {} days.".format(simulation.population, simulation.dayNumber))
        break
    if x is not simulation.daysToSimulate - 1:
        input("\nPress enter to advance to the next day...")

