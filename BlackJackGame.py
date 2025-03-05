from Deck import Deck
from Player import Player


class BlackjackGame:
    def __init__(self):
        # Holds all parameters required for Blackjack game
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player(is_dealer=True)

    def start_game(self):
        # Initial two cards for each player
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

        print("Dealing initial cards...\n")
        print("Here are your initial cards:")
        self.player.show_hand()

        # Show the dealer's hand with the first card hidden

        self.dealer.show_hand(hide_first_card=True)
        print("Dealer's initial hand (first card hidden):")
    def player_turn(self):
        # Allow the player to hit or stand.
        while self.player.calculate_hand_value() < 21:
            choice = input("Do you want to hit or stand?: ").lower()
            if choice == 'hit':
                self.player.add_card(self.deck.deal_card())
                self.player.show_hand()
                self.dealer.show_hand(hide_first_card=True)
                if self.player.calculate_hand_value() > 21:
                    print("You bust! Dealer wins.")
                    return False
            elif choice == 'stand':
                break
            else:
                print("Invalid input. Please try again.")
        return True

    def dealer_turn(self):
        # Dealer reveals hidden card and draws until reaching 17 or more.
        self.dealer.show_hand(hide_first_card=True)
        while self.dealer.calculate_hand_value() < 17:
            self.dealer.add_card(self.deck.deal_card())
            self.dealer.show_hand(hide_first_card=True)

    def determine_winner(self):
        player_score = self.player.calculate_hand_value()
        dealer_score = self.dealer.calculate_hand_value()

        print("\nFinal Hands:")
        self.player.show_hand()
        self.dealer.show_hand()

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