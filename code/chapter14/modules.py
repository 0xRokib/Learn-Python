# Importing built-in and custom modules
from math import pi  # Importing pi constant from math module
import sys  # System-related functions and parameters
import random as rdm  # Importing random module with alias
import kansas  # Importing the custom kansas module

# Printing the value of pi
print(f"Value of pi: {pi}")

# Using random.choice to pick a random character from the string '123'
print(f"Random choice: {rdm.choice('123')}")

# Uncomment the following lines to see all attributes and methods in the random module
# for item in dir(rdm):
#     print(item)

# Accessing variables from the kansas module
print(f"Kansas Capital: {kansas.capital}")

# Calling the function from kansas module
kansas.randomfunfact()

# Checking the special __name__ variable
print(f"__name__ in modules.py: {type(__name__)}")

# Printing the __name__ attribute of the imported kansas module
print(f"__name__ in kansas module: {kansas.__name__}")
