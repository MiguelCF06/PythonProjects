import random
import time

class Card:
    """Class where card is displayed"""
    def __init__(self, rank, value, suit):
        """Initialize its values"""
        self.rank = rank
        self.value = value
        self.suit = suit

    def displayCard(self):
        """Display the cards of the deck"""
        print("{} of {}".format(self.rank, self.suit))

class Deck:
    """Make a deck"""
    def __init__(self):
        """Initialize Values"""
        self.cards = []

    def buildDeck(self):
        """Build a deck of cards"""
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = {
            "A": 11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
        }
        for suit in suits:
            for key, value in ranks.items():
                card = Card(key, value, suit)
                self.cards.append(card)

    def shuffleDeck(self):
        """Shuffle the cards"""
        random.shuffle(self.cards)

    def dealCard(self):
        """Remove a card from the deck to be dealt"""
        card = self.cards.pop()
        return card

class Player:
    def __init__(self):
        """Initialize the values"""
        self.hand = []
        self.handValue = 0
        self.playingHand = True

    def drawHand(self, deck):
        """The players starting hand"""
        for x in range(2):
            card = deck.dealCard()
            self.hand.append(card)

    def DisplayHand(self):
        """Display the cards of the player"""
        print("\nPlayer's Hand.")
        for card in self.hand:
            card.displayCard()

    def hit(self, deck):
        """Take a card from the deck"""
        card = deck.dealCard()
        self.hand.append(card)

    def getHandValue(self):
        """Gets the values of the cards of the player"""
        self.handValue = 0
        aceInHand = False
        for card in self.hand:
            self.handValue += card.value
            if card.rank == "A":
                aceInHand = True
        if self.handValue > 21 and aceInHand:
            self.handValue -= 10
        print("The total value of the hand is {}.".format(self.handValue))

    def updateHand(self, deck):
        """Look for if the player wants to continue getting more cards"""
        if self.handValue < 21:
            choice = input("Would you like to hit? (y/n): ").lower()
            if choice == "y":
                self.hit(deck)
            else:
                self.playingHand = False
        else:
            self.playingHand = False

class Dealer:
    """The dealer class"""
    def __init__(self):
        """Initialize values"""
        self.hand = []
        self.handValue = 0
        self.playingHand = True

    def drawHand(self, deck):
        """The starting hand of the dealer"""
        for x in range(2):
            card = deck.dealCard()
            self.hand.append(card)

    def displayHand(self):
        """Displays the cards of the dealer"""
        input("\nPress enter to revel the dealer cards")
        for card in self.hand:
            card.displayCard()
            time.sleep(1)

    def getHandValue(self):
        """Gets the values of each card in the dealer's hand"""
        self.handValue = 0
        aceInHand = False
        for card in self.hand:
            self.handValue += card.value
            if card.rank == "A":
                aceInHand = True
        if self.handValue > 21 and aceInHand:
            self.handValue -= 10

    def hit(self, deck):
        """Allow the dealer to take another card to his hand"""
        self.getHandValue()
        while self.handValue < 17:
            card = deck.dealCard()
            self.hand.append(card)
            self.getHandValue()

class Game:
    def __init__(self, amountMoney):
        """Initialize values"""
        self.amountMoney = amountMoney
        self.bet = 20
        self.winner = ""

    def setBet(self):
        """Ask for the user for the amount of money to bet"""
        betting = True
        while betting:
            userBet = int(input("What is your bet? (minimum bet of $20): "))
            if userBet < 20:
                userBet = 20
            if userBet > self.amountMoney:
                print("You can't afford that bet!.\n")
            else:
                self.bet = userBet
                betting = False

    def scoring(self, playerHandValue, dealerHandValue):
        """The hand value score between player and dealer
        is compared for look for the winner"""
        if playerHandValue == 21:
            print("You've got Blackjack!!\n")
            self.winner = "P"
        elif dealerHandValue == 21:
            print("The dealer've got Blackjack!!\n")
            self.winner = "D"
        elif playerHandValue > 21:
            print("You went over 21!\n")
            self.winner = "D"
        elif dealerHandValue > 21:
            print("Dealer went over 21!\n")
            self.winner = "P"
        else:
            if playerHandValue > dealerHandValue:
                print("Dealer gets {}, You win!!!\n".format(dealerHandValue))
                self.winner = "P"
            elif playerHandValue < dealerHandValue:
                print("Dealer gets {}, Dealer wins!!!\n".format(dealerHandValue))
                self.winner = "D"
            else:
                print("Dealer gets {}, It's a tie!!!\n".format(dealerHandValue))
                self.winner = "Tie"

    def payout(self):
        """Depending of the winner the bet is added or substracted to the player's money"""
        if self.winner == "P":
            self.amountMoney += self.bet
        elif self.winner == "D":
            self.amountMoney -= self.bet

    def displayMoney(self):
        """Displays the money of the player"""
        print("The current money is: ${}.".format(self.amountMoney))

    def displayMoneyAndBet(self):
        """Displays the money and bet that the player did"""
        print("The current money is: ${}. Current Bet: ${}".format(self.amountMoney, self.bet))

print("Welcome to the Blackjack App.")
print("The minimum bet at this table is $20\n")

money = int(input("How much money would you like to place on the table: "))
game = Game(money)
playing = True

while playing:
    gameDeck = Deck()
    gameDeck.buildDeck()
    gameDeck.shuffleDeck()

    player = Player()
    dealer = Dealer()

    game.displayMoney()
    game.setBet()

    player.drawHand(gameDeck)
    dealer.drawHand(gameDeck)

    game.displayMoneyAndBet()
    print("The dealer is showing a {} of {}.".format(dealer.hand[0].rank, dealer.hand[0].suit))
    while player.playingHand:
        player.DisplayHand()
        player.getHandValue()
        player.updateHand(gameDeck)

    dealer.hit(gameDeck)
    dealer.displayHand()

    game.scoring(player.handValue, dealer.handValue)
    game.payout()

    if game.amountMoney < 20:
        playing = False
        print("Sorry, you ran out of money. Please try again!\n")
