import unittest
from unittest import TestCase

from BlackJackGame import BlackjackGame
from Card import Card
from Deck import Deck
from Player import Player

#Blaize
class TestDeck(TestCase):


    def test_deal_card(self):
        deck = Deck()
        initial_size = len(deck.cards) #initial size of deck is 52 before dealing
        card = deck.deal_card() #runs the deal card function
        self.assertIsNotNone(card)
        self.assertEqual(len(deck.cards),initial_size - 1) #subtracts one from the deck after it is dealt

    def test_shuffle(self):
        deck = Deck()
        initial_size = len(deck.cards) #initial size 52
        deck.shuffle() #shuffles deck
        expected = 52 #should still be 52 cards
        self.assertEqual(initial_size,expected)
#Blaize
class TestCard(TestCase):


    def test_get_value1(self):
        jack = Card('Jack','Hearts') #Jack is not a integer so we need to get an in for it.
        result = jack.get_value() #gets the value of Jack
        expected = 10 #jacks value is 10
        self.assertEqual(result,expected) #expected in 10

    def test_get_value(self):
        ace = Card('Ace','Spades')
        result = ace.get_value() #gets the value of ace
        expected = 11 # ace value = 11
        self.assertEqual(result,expected) #expected is 11
#Manny
class TestPlayer(TestCase):

    def test_add_card1(self):
        player = Player() #gives an empty player hand
        card1 = Card('5','Hearts') #sets what card1 is equal too
        player.add_card(card1) #gives player the first card
        expected = 1 #expects that the player has 1 card now
        self.assertEqual(len(player.hand),expected)

    def test_add_card2(self):
        player = Player() #sets empty list
        card1 = Card('Jack','Hearts')
        card2 = Card('Queen','Clubs') #defines card1 and card2
        player.add_card(card1)
        player.add_card(card2) #adds card1 and card2
        expected = 2 #expects two cards to be in player()
        self.assertEqual(len(player.hand),expected)

    def test_calculate_hand_value1(self):
        player = Player() #sets empty list
        player.hand = [Card('Ace','Spades'),Card('King','Hearts')] #gives 2 cards
        result = player.calculate_hand_value() #calculates value of the 2 cards
        expected = 21 #calculated value = 21 so 21 is the expected result
        self.assertEqual(result,expected)

    def test_calculate_hand_value2(self):
        player = Player() #sets empty list
        #adds 3 cards to players hand
        player.hand = [Card('Ace','Hearts'),Card('4','Clubs'),Card('Jack','Spades')]
        result = player.calculate_hand_value() #calculates value of the 3 cards
        expected = 15 #calulated value = 15 so that is the expected
        self.assertEqual(result,expected)
#Manny
class TestBlackJackGame(TestCase):

    def test_start_game(self):
        game = BlackjackGame()
        game.start_game() #starts game
        self.assertEqual(len(game.player.hand),2) #adds 2 cards to player
        self.assertEqual(len(game.dealer.hand), 2) #adds 2 cards to dealer
        self.assertEqual(len(game.deck.cards), 52 - 4) #calculates the amount of cards that are
        # left in the deck after the game is started.



if __name__ == '__main__':
    unittest.main()




        




    