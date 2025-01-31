import sys
import random
from enum import Enum

# Define an enumeration for Rock, Paper, and Scissors choices
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True  # Flag to control the game loop

while playagain:
    # Prompt the player for input
    player_choice = input("\nEnter....\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
    
    # Convert input to integer and validate
    try:
        player = int(player_choice)
        if player not in [1, 2, 3]:
            sys.exit('You must choose 1, 2, or 3')
    except ValueError:
        sys.exit('Invalid input! Please enter a number (1, 2, or 3)')

    # Computer randomly selects Rock, Paper, or Scissors
    computer = random.randint(1, 3)

    # Display the choices
    print(f'You chose {RPS(player).name}.')
    print(f'Computer chose {RPS(computer).name}.')

    # Determine the winner based on game rules
    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2): 
        print('You win!')
    elif player == computer:  
        print('Tie Game!')
    else: 
        print('Python wins!')
        
    # Ask player if they want to play again
    playagain = input("\nPlay again? \nY for Yes or \nQ for Quit.\n\n").strip().lower()
    if playagain == 'y':
        continue
    else:
        print("Thank You For Playing the Game!\n")
        playagain = False

# Exit the program
sys.exit("Bye!")