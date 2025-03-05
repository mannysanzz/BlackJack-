Blackjack Game:

Card.py: This file takes the rank and the suit from Deck.py and assigns a value to it
It sets the face cards equal to 10 besides jack which is equal to 11(and one in some
cases as defined in player.py) Then it returns the value of the card and shows it's
rank as well

Player.py: It defines the player and the dealers hand and sets there totals to zero.
Then it adds another card when either the player or the dealer decides to hit. Next it
calculates what the total of the hand is after the hit and decides of the ace has to be
a 10 or a 1 depending on the total score. Next it prints the dealer or players hand
depending on who last hit. It then shows the dealers hidden card and decides whether
to show the total hand value.

Game.py: First it lets the user decide when to start the game by hitting enter in the
terminal. It then starts the game and dishes out the dealers cards then the players
cards and runs through the players and dealers hits or stands. Finally it determines
the winner and displays it.




Class Deck.py
This file creates the Deck Class, which creates a full deck of 52 cards.
-Blueprint
     __init__(self: rank,suit) Function initializes a Card with a rank and suit.

     __str__(self) Returns a string of the player and dealers cards.

     def(shuffle) Calls python's randomizing function that shuffles cards.

     def deal_card()

BlackJackGame.py
This file contains the main game logic importing classes from other files.

    __innit__() Initializes a new deck, player and dealer.

    def start_game() Starts the game by dealing two cards to player and dealer.

    def player_turn() Prompts user to either hit or stand depending on the cards that they received.

    def dealer_turn() Handles whether the dealer hits or stands depending on the cards it was dealt.

    def determine_winner() Compares the cards of the player and dealer and determines the winner and prints the results.

Lists used:

    In Deck.py
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # List of suits the cards will be of

    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # Determines what cards will be in the deck

    self.cards = [] # Creates list of 52 each with their own unique suit and rank

    In Player.py
    self.hand = [] # Makes a list of cards player receives

