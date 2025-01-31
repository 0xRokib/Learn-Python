# Basic While Loop
num = 1
while num < 10:
    print(num)
    if num == 5:
        break  # Exit loop when num is 5
    num += 1

# While Loop with Continue and Else
counter = 1
while counter <= 10:
    counter += 1
    if counter == 5:
        continue  # Skip printing when counter is 5
    print(counter)
else:
    print("Counter is now equal to", counter)


# For loop through a list of names
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

# Looping through a string
word = "Python"
for ch in word:
    print(ch)

# For loop with break using a different list
cities = ['New York', 'Paris', 'London', 'Tokyo']
for city in cities:
    if city == "Paris":
        break  # Exit loop when city is Paris
    print(city)

# For loop with continue using a different list
colors = ['Red', 'Green', 'Blue', 'Yellow']
for color in colors:
    if color == "Green":
        continue  # Skip Green and continue iteration
    print(color)

# For loop with range
for i in range(5):  # 0 to 4
    print(i)

for x in range(2, 5):  # 2 to 4
    print(x)

for x in range(5, 101, 5):  # Multiples of 5 from 5 to 100
    print(x)
else:
    print("Glad That's over!")


# Nested loop: Different actions performed by different animals
animals = ['dog', 'cat', 'rabbit']
actions = ['runs', 'jumps', 'sleeps']

for action in actions:
    for animal in animals:
        print(f"The {animal} {action}.")


# Looping through a dictionary
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 88}

# Loop through keys
for student in student_scores:
    print(student)

# Loop through values
for score in student_scores.values():
    print(score)

# Loop through key-value pairs
for student, score in student_scores.items():
    print(f"{student} scored {score}")
