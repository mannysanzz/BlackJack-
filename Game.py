#Emmanuel Sanchez
import BlackJackGame


def main():
    # Sets a break before initializing the game, prompting users to enter if they want to play
    input("Press Enter to start your turn...")
    # Creates an instance of the game from BlackJack class
    game = BlackJackGame.BlackjackGame()
    # Initializing function from BlackJack class therefore dealing cards
    game.start_game()

    # Initializes players turn prompting user to either hit or stand
    if game.player_turn():
        # If player does not bust, dealer's turn is initialized
        game.dealer_turn()

    # After turns are done winner is determined.

    game.determine_winner()


if __name__ == "__main__":
    main()