import sys
import random
from enum import Enum

# Define an enumeration for Rock, Paper, and Scissors choices
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Prompt the player for input
print("")
player_choice = input("Enter....\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
player = int(player_choice)

# Validate player input (must be 1, 2, or 3)
if player < 1 or player > 3:
    sys.exit('You must choose 1, 2, or 3')

# Computer randomly selects Rock, Paper, or Scissors
computer_choice = random.choice('123') 
computer = int(computer_choice)  

# Display the choices
print('You chose ' + str(RPS(player)).replace("RPS.", "") + '.')
print('Computer chose ' + str(RPS(computer)).replace("RPS.", "") + '.')

# Determine the winner based on game rules
if player == 1 and computer == 3: 
    print('You win!')
elif player == 2 and computer == 1: 
    print('You win!')
elif player == 3 and computer == 2: 
    print('You win!')
elif player == computer:  
    print('Tie Game!')
else: 
    print('Python win!')
