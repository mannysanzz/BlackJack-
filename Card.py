# Defines the card class which represents a playing card in our case
class Card:
    # Initializes a new card object with a rank and suit
    def __init__(self, rank, suit):
        self.rank = rank # Card rank ex. 1,2,3...
        self.suit = suit # Card suit ex. Spades, Clubs...
    # Str method returns a string representation of Card
    def __str__(self):
        # Ex. "7 of Spades"
        return f"{self.rank} of {self.suit}"
    # Gets numerical value of Card
    def get_value(self):
        # If card is Jack, Queen, King value is assigned to 10
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        # Gives Ace a numerical value
        elif self.rank == 'Ace':

            return 11
        else:
            # If Card is not Jack, Queen, King and Ace, integer value of rank is returned
            return int(self.rank)


