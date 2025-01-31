# Python Loops

Loops in Python allow you to execute a block of code multiple times. Python supports two types of loops:

- `while` loop
- `for` loop

## 1. While Loop

The `while` loop executes a block of code as long as a condition is true.

### Example 1: Basic While Loop

```python
value = 1
while value < 10:
    print(value)
    if value == 5:
        break  # Terminates the loop when value is 5
    value += 1
```

### Example 2: While Loop with Continue and Else

```python
value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue  # Skips the rest of the loop for value == 5
    print(value)
else:
    print("Value is now equal to " + str(value))
```

## 2. For Loop

The `for` loop iterates over a sequence (like a list, string, or range).

### Example 1: Looping Through a List

```python
names = ['Rokib', 'Sarah', 'John']
for name in names:
    print(name)
```

### Example 2: Looping Through a String

```python
for ch in "Rokib":
    print(ch)
```

### Example 3: Using `break` in a For Loop

```python
names = ['Rokib', 'Sarah', 'John']
for name in names:
    if name == "Sarah":
        break  # Stops the loop when name is Sarah
    print(name)
```

### Example 4: Using `continue` in a For Loop

```python
names = ['Rokib', 'Sarah', 'John']
for name in names:
    if name == "Sarah":
        continue  # Skips Sarah and continues with the next iteration
    print(name)
```

## 3. For Loop with `range()`

`range(start, stop, step)` generates a sequence of numbers.

### Example 1: Iterating Over a Range

```python
for i in range(5):
    print(i)  # Outputs numbers from 0 to 4
```

### Example 2: Specifying Start and Stop

```python
for x in range(2, 5):
    print(x)  # Outputs 2, 3, 4
```

### Example 3: Using Step Value

```python
for x in range(5, 101, 5):
    print(x)  # Outputs multiples of 5 from 5 to 100
else:
    print("Glad That's over!")
```

## 4. Nested Loops

A loop inside another loop is called a nested loop.

### Example: Nested Loops with Lists

```python
names = ['rokib', 'hasan', 'tani']
actions = ['codes', 'eats', 'sleeps']

for action in actions:
    for name in names:
        print(name + " " + action + ".")
```

## 5. Looping Through a Dictionary

You can loop through a dictionary's keys, values, or key-value pairs.

### Example 1: Looping Through Keys

```python
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 88}
for student in student_scores:
    print(student)  # Outputs only the keys
```

### Example 2: Looping Through Values

```python
for score in student_scores.values():
    print(score)  # Outputs only the values
```

### Example 3: Looping Through Key-Value Pairs

```python
for student, score in student_scores.items():
    print(f"{student} scored {score}")
```

## Conclusion

Loops are fundamental in Python and allow efficient iteration over data structures. Understanding `while` loops, `for` loops, `range()`, and dictionary looping will help you write cleaner and more effective code.

Happy coding! 🚀
