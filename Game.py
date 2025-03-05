import BlackJackGame


def main():
    input("Press Enter to start your turn...")
    game = BlackJackGame.BlackjackGame()  # Create a game instance.
    game.start_game()  # Deal initial cards.

    # Player's turn.
    if game.player_turn():
        # Only if the player hasn't busted.
        game.dealer_turn()

    # Determine and display the winner.
    game.determine_winner()


if __name__ == "__main__":
    main()