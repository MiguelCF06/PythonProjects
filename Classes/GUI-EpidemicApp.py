import tkinter
import math
import random


class Simulation:
    def __init__(self):
        self.dayNumber = 1
        print("We must to know the population size.")
        self.population = int(input("---Enter the popuation size: "))
        root = math.sqrt(self.population)
        if int(root + .5) ** 2 != self.population:
            root = round(root, 0)
            self.gridSize = int(root)
            self.population = self.gridSize ** 2
            print("Rounding population size to {} for visual purposes.".format(self.population))
        else:
            self.gridSize = int(math.sqrt(self.population))
        print("\nWe must first start by infecting a portion of the population.")
        self.infectionPercent = float(
            input("---Enter the percentage (0-100) of the population to initially infected: "))
        self.infectionPercent /= 100

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infectionProbability = float(input("---Enter the probability (0-100) that a person gets infected \
when exposed to the disease: "))
        print("We must know how long the infection will last when exposed.")
        self.infectionDuration = int(input("---Enter the duration (in days) of the infection: "))

        print("\nWe must know the mortality rate of those infected.")
        self.mortalityRate = float(input("---Enter the mortality rate (0-100) of the infection: "))

        print("\nWe must know how long to run the simulation.")
        self.simDays = int(input("---Enter the number of days to simulate: "))


class Person:
    def __init__(self):
        self.isInfected = False
        self.isDead = False
        self.daysInfected = 0

    def infect(self, simObj):
        chanceToBeInfected = random.randint(0, 100)
        if chanceToBeInfected < simObj.infectionProbability:
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
                if mortalityRate < simObj.mortalityRate:
                    self.die()
                elif self.daysInfected == simObj.infectionDuration:
                    self.heal()


class Population:
    def __init__(self, simulation):
        self.population = []
        for i in range(simulation.gridSize):
            row = []
            for j in range(simulation.gridSize):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initialInfection(self, simulation):
        infectedCount = int(round(simulation.infectionPercent * simulation.population, 0))
        infections = 0
        while infections < infectedCount:
            x = random.randint(0, simulation.gridSize - 1)
            y = random.randint(0, simulation.gridSize - 1)
            if not self.population[x][y].isInfected:
                self.population[x][y].isInfected = True
                self.population[x][y].daysInfected = 1
                infections += 1

    def spreadInfection(self, simulation):
        for i in range(simulation.gridSize):
            for j in range(simulation.gridSize):
                if not self.population[i][j].isDead:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j + 1].isInfected or self.population[i + 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.gridSize - 1:
                            if self.population[i][j - 1].isInfected or self.population[i + 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j - 1].isInfected or self.population[i][j + 1].isInfected \
                                    or self.population[i + 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                    elif i == simulation.gridSize - 1:
                        if j == 0:
                            if self.population[i][j + 1].isInfected or self.population[i - 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.gridSize - 1:
                            if self.population[i][j - 1].isInfected or self.population[i - 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j - 1].isInfected or self.population[i][j + 1].isInfected \
                                    or self.population[i - 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                    else:
                        if j == 0:
                            if self.population[i][j + 1].isInfected or self.population[i + 1][j].isInfected \
                                    or self.population[i - 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.gridSize - 1:
                            if self.population[i][j - 1].isInfected or self.population[i + 1][j].isInfected \
                                    or self.population[i - 1][j].isInfected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j - 1].isInfected or self.population[i + 1][j].isInfected \
                                    or self.population[i + 1][j].isInfected or self.population[i - 1][j]:
                                self.population[i][j].infect(simulation)

    def update(self, simulation):
        simulation.dayNumber += 1
        for row in self.population:
            for person in row:
                person.update(simulation)

    def displayStatistics(self, simulation):
        totalInfected = 0
        totalDeaths = 0
        for row in self.population:
            for person in row:
                if person.isInfected:
                    totalInfected += 1
                    if person.isDead:
                        totalDeaths += 1
        infectedPercent = round(100 * (totalInfected / simulation.population), 4)
        deathPercent = round(100 * (totalDeaths / simulation.population), 4)

        print("\n-----Day #{}-----".format(simulation.dayNumber))
        print("Percentage of Population Infected: {}%".format(infectedPercent))
        print("Percentage of Population Dead: {}%".format(deathPercent))
        print("Total People Infected: {} / {}".format(totalInfected, simulation.population))
        print("Total Deaths: {} / {}".format(totalDeaths, simulation.population))


def graphics(simulation, population, canvas):
    squareDimension = 800 // simulation.gridSize
    for i in range(simulation.gridSize):
        y = i * squareDimension
        for j in range(simulation.gridSize):
            x = j * squareDimension
            if population.population[i][j].isDead:
                canvas.create_rectangle(x, y, x + squareDimension, y + squareDimension, fill="red")
            else:
                if population.population[i][j].isInfected:
                    canvas.create_rectangle(x, y, x + squareDimension, y + squareDimension, fill="yellow")
                else:
                    canvas.create_rectangle(x, y, x + squareDimension, y + squareDimension, fill="green")


sim = Simulation()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

simWindow = tkinter.Tk()
simWindow.title("Epidemic Outbreak")
simCanvas = tkinter.Canvas(simWindow, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
simCanvas.pack(side=tkinter.LEFT)

population = Population(sim)

population.initialInfection(sim)
population.displayStatistics(sim)
input("Press enter to begin the simulation...")

for i in range(1, sim.simDays):
    population.spreadInfection(sim)
    population.update(sim)
    population.displayStatistics(sim)
    graphics(sim, population, simCanvas)
    simWindow.update()
    if i == sim.simDays - 1:
        simCanvas.wait_visibility()
