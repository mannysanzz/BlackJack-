class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    # Gives cards numerical values
    def get_value(self):
        # If card is Jack, Queen, King value is assigned to it
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        # Gives Ace a numerical value
        elif self.rank == 'Ace':

            return 1
        else:
            return int(self.rank)


