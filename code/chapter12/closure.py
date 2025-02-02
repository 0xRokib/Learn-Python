def create_player(person, initial_coins):
    """
    Initializes a player with a given number of coins.
    Returns a function that decrements the player's coins when called.
    """
    coins = initial_coins  # coins is now local to the created player

    def play_game():
        nonlocal coins  # Access the coins variable from the enclosing scope
        coins -= 1  # Decrease the coin count by 1

        # Display appropriate message based on the remaining coins
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of the game.")
    
    return play_game  # Return the inner function to be used as a player's action

# Create individual player functions
player_tommy = create_player('Tommy', 3)
player_jenny = create_player('Jenny', 5)

# Simulating game actions
player_tommy()
player_tommy()
player_jenny()
player_tommy()
