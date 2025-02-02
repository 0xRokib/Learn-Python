import sys
import random
from enum import Enum
game_count = 0

def play_rps():
    # Define Rock, Paper, Scissors as an Enum
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Get player's choice with validation
    player_choice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n").strip()
    
    if player_choice not in ['1', '2', '3']:
        print("Invalid input! You must enter 1, 2, or 3.")
        return play_rps()  # Recursive call for invalid input

    player = int(player_choice)
    computer = random.randint(1, 3)

    # Display choices
    print(f"\nYou chose {RPS(player).name}.")
    print(f"Computer chose {RPS(computer).name}.")

    # Determine winner
    def decide_winner(player, computer):
        if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
           return "🎉 You win!"
        elif player == computer:
           return "😲 Tie game!"
        else:
           return "🐍 Python wins!"
    game_result = decide_winner(player, computer)
    print(game_result)
        
    global game_count
    game_count += 1
    
    print("\nGame Count: " + str(game_count))

    # Ask if the player wants to play again
    playagain = input("\nPlay again? (Y for Yes, Q to Quit): ").strip().lower()

    if playagain == 'y':
        return play_rps()  # Recursive call for replay
    elif playagain == 'q':
        print("\n🎉 Thank You For Playing! 🎉\n")
        sys.exit("Bye! 👋")
    else:
        print("Invalid input! Enter 'Y' to play again or 'Q' to quit.")
        return play_rps()  # Recursive call for invalid replay input

# Start the game
play_rps()
