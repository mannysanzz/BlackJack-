# Blaize Hatfield
# Imports the random module from pycharm
import random
# Imports Card class from Card.py
from Card import Card

# Creates Deck class that represents a collection of cards
class Deck:
    # Initializes a deck object with a full set of playing cards
    def __init__(self):

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # Defines the list of possible card suits
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # Defines list of possible card ranks
        # Creates list
        self.cards = []
        # Loops through the suit list
        for suit in suits:
            # Loops through the rank list as a nested loop within rank
            for rank in ranks:
                # Creates a new card object with every possibility of rank and suit and appends it to the deck
                self.cards.append(Card(rank,suit))

        # Calls the randomizing module into the code by shuffle(used for lists)
        self.shuffle()
    # Uses shuffle to randomize the list of cards
    def shuffle(self):
        random.shuffle(self.cards)
    # Function that deals cards, Represents the Deck function allowing to attributes like Cards
    def deal_card(self):
        # Conditional statements that returns a card object if list is not empty
        # Pop removes and returns the last element of Deck
        return self.cards.pop() if self.cards else None
