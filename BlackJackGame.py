# Emmanuel Sanchez
# Imports Deck class from Deck.py
from Deck import Deck
# Imports Player class from Player.py
from Player import Player

# Creates BlackJack class that contains the games logic
class BlackjackGame:
    # Initializes the game with a new deck, player(user) and dealer
    def __init__(self):
        # Creates all these parameters
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player(is_dealer=True)
    # Function initializes the game
    def start_game(self):
        # Initial two cards for each player
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

        print("Dealing initial cards...\n") # Print statement imitates being dealt two cards
        print("Here are your initial cards:") # Print statement acts as header for cards you are dealt
        self.player.show_hand() # Function from player class that

        # Calculates players total and prints it
        player_total = self.player.calculate_hand_value()
        print("Your current score is:", player_total)

        # Show the dealer's hand with the first card hidden
        self.dealer.show_hand(hide_first_card=True)
        print("Dealer's initial hand (first card hidden):")

        dealer_total = self.dealer.calculate_hand_value()
        print("Dealer's current score is:", dealer_total)

    # Function initializes players turn
    def player_turn(self):

        while True:
            # Calculates the players current hand value
            player_total = self.player.calculate_hand_value()
            # If players hand value is greater than or equal to 21 player is not allowed to hit
            if player_total >= 21:
                break
            # Prompts player to either hit or stand and sets result equal to choice
            choice = input("\nDo you want to hit or stand? (hit/stand): ").lower()
            # If players choice is equal to hit:
            if choice == 'hit':
                # New card is dealt to player
                new_card = self.deck.deal_card()
                # Prints what card is received
                print("You received: " + str(new_card))
                # Adds new card to player hand
                self.player.add_card(new_card)
                # Shows players hand with new card added
                self.player.show_hand()
                # If players total card value with new card is greater than 21 then game stops
                if self.player.calculate_hand_value() > 21:
                    # Prints in terminal that game is over
                    print("You bust! Dealer wins.")
                    return False
            # If players choice is equal to stand then their turn is over
            elif choice == 'stand':
                break
            # If invalid choice is inputted, print statement prompts user to try again
            else:
                print("Invalid input. Please try again.")
        return True
    # Function handles dealers turn
    def dealer_turn(self):
        # Dealer's hand is shown first
        self.dealer.show_hand(hide_first_card=True)
        # While the dealers hand is less than 17 he draws cards
        while self.dealer.calculate_hand_value() < 17:
            # New card is added to the dealers hand
            self.dealer.add_card(self.deck.deal_card())
            # Displays new hand while hiding first card
            self.dealer.show_hand(hide_first_card=True)
    # Function contains possible outcomes to determine who is the winner of the game
    def determine_winner(self):
        # Calculates total for player and dealers final hand
        player_score = self.player.calculate_hand_value()
        dealer_score = self.dealer.calculate_hand_value()

        # Prints header to indicate final hands
        print("\nFinal Hands:")
        # Displays player and dealers hand
        self.player.show_hand()
        self.dealer.show_hand()

        # Determines and prints game results based on scores
        if player_score > 21:
            print("Dealer wins! (Player busts)")
        elif dealer_score > 21:
            print("Player wins! (Dealer busts)")
        elif player_score > dealer_score:
            print("Player wins!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")