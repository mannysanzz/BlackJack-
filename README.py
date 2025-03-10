Blackjack Game:

Game.py
This is the driver file that is used to run the project.
This file contains the main() function that initializes the blackjack game, it manages the flow of the game
(starting the game, handling turns, and determining the winner)

Card.py:
This file takes the rank and the suit from Deck.py and assigns a value to it
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
This file creates the Deck Class, which creates a full deck of 52 card objects.
It creates a standard 52 card deck and deals one card at a time.
The methods of this class include, __init__ , shuffle() and deal_card



BlackJackGame.py
This file contains the main game logic importing classes from other files.
This class initializes the deck, player and dealer, and starts the game by dealing two cards to each player.
Also manages the players turn(hit/stand decisions)
Determines the outcome of the game by displaying the outcome.

Lists used:

    In Deck.py
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # List of suits the cards will be of

    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # Determines what cards will be in the deck

    self.cards = [] # Creates list of 52 each with their own unique suit and rank

    In Player.py
    self.hand = [] # Makes a list of cards player receives


Blueprints of Classes

--Card Class--

Attributes:
    Rank: str (Ace,King,1,2,3)
    Suit: str(Hearts, Spades, Clubs, Diamonds)

Methods:
    __init__(self, rank: str, suit: str) -> None
    __str__(self) -> str
    def get_value(self) -> int
        # This function takes the string value of a card and turns it into an integer.

--Deck Class--

Attributes:
    cards: list[Card] (list of Card objectives; initially 52 cards)

Methods:
    __init__(self) -> None (Creates the deck and shuffles it)
    def shuffle(self) -> None
        # This function uses pythons method of randomization to shuffle the cards.
          For our project we use shuffle because we are randomizing a list of cards.
    def deal_card(self) -> Card or none
        # This function "deals" a card by removing one card from the deck and returns None if list is empty

--Player Class--

Attributes:
    hand: list[Card] These are the cards in the players hand
    is_dealers: bool This attribute is true if the players hand is the dealer

Methods:
    __init__(self, is dealer: bool = False) -> None
    def add_card(self, Card) -> None
        # Appends card to players hand
    def calculate_hand_value(self) -> int
        # Returns an integer of the total hand value
    def show_hand(self)
        # This function shows a string representation of the hand

--BlackJackGame Class--

Attributes:
    deck: Deck
    player: player
    dealer: Dealer

Methods:
    __init__(self) -> None
    def start_game(self) -> None
        # Initializes the game
    def player_turn(self) -> None
        # Starts the players turn
    def dealer_turn(self) -> None
         # starts the dealers turn
    def determine_winner(self)
        # Calculates the players cards and determines the winner


Function Blueprint:

Card.py

def __init__(self,rank: str, suit: str) -> None:
    # Initializes a card object with a given rank and suit
    # rank: str - rank of card
    # suit: - suit of the card
    # Returns None

def __str__(self) -> str
    # Returns a readable string representation of the card
    # Returns str("rank" of "suit")

def get_value(self) -> int:
    # This function returns a numerical value of the card
    # returns integer - 10 for face cards, 11 for Ace and numerical value ofr all other number cards

Deck.py

def __init__(self) -> None:
    # This function creates a new deck of 52 cards and shuffles them
    # Returns None

def shuffle(self) -> None
    # This function randomizes the order of cards in the deck
    # Returns none

def deal_card(self) -> Card or None
    # This function removes and returns the top card from the newly created Deck
    # Returns a Card or None if deck is empty

Player.py

def __init__(self, is_dealer=False) -> None
    # initializes a new Player in the game
    # Creates an empty list that serves as the players hand
    Returns None

def add_card(self, card:Card) -> None
    # This function adds a card to the player's hand
    # Returns None

def_calculate_hand_value(self) -> int:
    # This function computes the total value of the player's hand
    # Returns an integer value of the total hand value, adjusting Ace as necessary

def show_hand(self, hide_first_card = False) -> None:
    # This function prints the player's hand in the terminal
    # hide_first_card applies if player is the dealer, The dealer's first card is hidden
    # Returns None

--BlackJackGame Class--
def init(self):
    #creates the deck
    #creates a player
    #creates another player then sets that player as the dealer

def start_game(self):
    #adds card to players hand
    #adds card to players hand
    #adds card to dealers hand
    #adds card to dealers hand
    #prints statement that player is getting delt cards
    #prints statement here are your initial cards
    #calculates players total hand value
    #hides one of the dealers cards
    #prints dealers initial hand excluding the first card
    #calculates dealers total hand value
    #shows player the dealers hand value

def player_turn
    #calculates players total hand value\
    #sees if players hand is >= to 21
    #If it isn't it asks player to hit or stand
    #if players chooses hit then it deals another card
    #adds new card to there hand
    #shows new card in there hand
    #calculates if the new hand value is >=21
    #if it is it prints you bust
    #if it isn't gives them the option to hit or stand again and goes back to top
    #if stand end turn

def dealer_turn
    #shows dealers hand but not the first card
    #Calculates if dealers hand is <17
    #If yes then hit
    #If not then stand


def determine_winner(self) -> str
    # This function compares the player's and dealer's hands and determines the game outcome based on them
    # Returns a string message indicating who won or if game is a tie