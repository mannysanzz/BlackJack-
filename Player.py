# Defines Player class that is used for both player and dealer
class Player:
    # Initializes the players hand and flags whether player is dealer
    def __init__(self, is_dealer=False):
        # Creates a list for users hand
        self.hand = []
       #
        self.is_dealer = is_dealer
   # This function adds a new card to the players hand
    def add_card(self, card):
        # Appends card to list
        self.hand.append(card)
    # Function computes total value of players hand
    def calculate_hand_value(self):
            # Total is set to 0 at first
            total = 0
            # Runs through the Cards in players hand
            for card in self.hand:
                # Adds the cards integer value to the total
                total += card.get_value()
            # Counts Aces in hand
            ace_count = 0
            for card in self.hand:
                if card.rank == 'Ace': # Checks if Card in hand is an ace
                    ace_count += 1 # Adds to the ace count in hand
            # Adjust Ace value if total > 21
            while total > 21 and ace_count > 0:
                total -= 10 # If ace value is greater than 1o than ace value is automatically set to 1
                ace_count -= 1 # Subtracts the number of aces to adjust if more than one ace is in hand
            # Returns total calculated hand value
            return total
    # function displays the players cards
    def show_hand(self, hide_first_card=False):
        # Prints header indicating which players cards they are
        if self.is_dealer:
            print("\nDealer's Hand:")
        else:
            print("\nPlayer's Hand:")

        # Loop through each card in the hand and prints it
        for i in range(len(self.hand)):
            # This if statement applies to the first card in the dealers hand
            if i == 0 and hide_first_card and self.is_dealer:
                # Prints hidden Card for index 0 (first card) of the dealer
                print("Hidden Card")
            else:
                # If player is not dealer then first card is shown
                print(self.hand[i])

        # Determine if we should display the card and hand value if player is not dealer
        if not hide_first_card or not self.is_dealer:
            total = self.calculate_hand_value() # Calls the calculate hand value and sets it equal to total
            print("Total value:", total) # Prints total value of cards in hand

