import random

from Card import Card

#shows the card number and suit when a card is played
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        self.shuffle()
#shuffles the cards using pycharm randomizing tool
    def shuffle(self):
        random.shuffle(self.cards)
#deals cards
    def deal_card(self):
        return self.cards.pop() if self.cards else None
