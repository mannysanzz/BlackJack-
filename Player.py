class Player:
    def __init__(self, is_dealer=False):
        # defines users hand
        self.hand = []
        # Defines dealers hand
        self.is_dealer = is_dealer
#adds next card after player/dealer decides to hit
    def add_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = sum(card.get_value() for card in self.hand)

        aces = sum(1 for card in self.hand if card.rank == 'Ace')
        # Adjust Ace from 11 to 1 as needed
        while aces > 0 and value + 10 <= 21:
            value += 10
            aces -= 1
        return value

    def show_hand(self, hide_first_card=False):
        print(f"\n{'Dealer' if self.is_dealer else 'Player'}'s Hand:")
        for i, card in enumerate(self.hand):
            if i == 0 and hide_first_card and self.is_dealer:
                print("Hidden Card")
            else:
                print(card)
        # Only show total value if not hiding the dealer's first card.
        if not hide_first_card or not self.is_dealer:
            print(f"Total value: {self.calculate_hand_value()}")
