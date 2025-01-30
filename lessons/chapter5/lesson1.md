# Chapter 5 - User Input & Control Flow

## Rock-Paper-Scissors Game

This project is a simple Rock-Paper-Scissors game implemented in Python. It demonstrates how to handle user input, control flow, and randomness in Python programs.

---

## Topics Covered

### 1. **User Input (`input()`)**

- The game takes user input using `input()` and converts it into an integer.
- Example:
  ```python
  player_choice = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: ")
  player = int(player_choice)
  ```

### 2. **Control Flow (`if-elif-else`)**

- The game logic is determined using conditional statements to check who wins.
- Example:
  ```python
  if player == 1 and computer == 3:
      print('You win!')
  elif player == computer:
      print('Tie Game!')
  else:
      print('Python wins!')
  ```

### 3. **Enumerations (`Enum`)**

- The `Enum` class is used to define constant values for Rock, Paper, and Scissors.
- Example:
  ```python
  from enum import Enum
  class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3
  ```

### 4. **Random Module (`random.choice()`)**

- The computer randomly selects Rock, Paper, or Scissors using `random.choice()`.
- Example:
  ```python
  import random
  computer_choice = random.choice('123')
  computer = int(computer_choice)
  ```

### 5. **Program Exit (`sys.exit()`)**

- If the user enters an invalid choice, the program exits using `sys.exit()`.
- Example:
  ```python
  import sys
  if player < 1 or player > 3:
      sys.exit('You must choose 1, 2, or 3')
  ```

---

## Game Code Explanation

```python
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
player_choice = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: ")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit('You must choose 1, 2, or 3')

computer_choice = random.choice('123')
computer = int(computer_choice)

print('You chose ' + str(RPS(player)).replace("RPS.", "") + '.')
print('Computer chose ' + str(RPS(computer)).replace("RPS.", "") + '.')

if player == 1 and computer == 3:
    print('You win!')
elif player == 2 and computer == 1:
    print('You win!')
elif player == 3 and computer == 2:
    print('You win!')
elif player == computer:
    print('Tie Game!')
else:
    print('Python wins!')
```

---

## How to Run the Game

1. Install Python (if not already installed).
2. Copy the above code into a file (e.g., `rps_game.py`).
3. Open a terminal and navigate to the file location.
4. Run the command:
   ```bash
   python rps_game.py
   ```
5. Follow the on-screen instructions to play the game.

---

## Conclusion

This project demonstrates fundamental programming concepts such as user input handling, control flow, enumerations, and randomness in Python. It serves as a great introduction to building interactive console applications.
