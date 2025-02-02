import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
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
            nonlocal player_wins
            nonlocal python_wins
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"
        game_result = decide_winner(player, computer)
        print(game_result)
            
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer Wins: {str(player_wins)}")
        print(f"\nPython Wins: {str(python_wins)}")

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

    return play_rps()


play = rps()
play()