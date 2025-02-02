# String Formatting in Python

# Defining variables
person = "Rokib"
coins = 3 

# Using the old % formatting method
message = "\n%s has %s coins left." % (person, coins)
print(message)

# Using the str.format() method
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# Changing order of placeholders
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

# Using named placeholders
message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

# Formatting with a dictionary using unpacking (** operator)
player = {"person": "Rokib", "coins": 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# Using f-strings (Python 3.6+)
message = f"\n{person} has {coins} coins left."
print(message)

# Applying a method inside an f-string
message = f"\n{person.lower()} has {coins} coins left."
print(message)

# Accessing dictionary values in f-strings
message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

# Formatting numbers inside f-strings
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# Looping through numbers and formatting output
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
    
# Formatting as a percentage
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")