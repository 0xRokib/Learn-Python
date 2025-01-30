# Python Operators

## Assignment Operators

Assignment operators are used to assign values to variables and modify them using shorthand notations.

- `=` Assigns a value to a variable.
- `+=` Adds and assigns a value.
- `-=` Subtracts and assigns a value.
- `*=` Multiplies and assigns a value.
- `/=` Divides and assigns a value.

```python
x = 10
x += 5  # Equivalent to x = x + 5
x -= 3  # Equivalent to x = x - 3
x *= 2  # Equivalent to x = x * 2
x /= 4  # Equivalent to x = x / 4
```

## Arithmetic Operators

Arithmetic operators perform basic mathematical operations.

- `+` Adds two values.
- `-` Subtracts one value from another.
- `*` Multiplies two values.
- `/` Divides one value by another.
- `//` Performs floor division.
- `%` Returns the remainder of division.
- `**` Raises one value to the power of another.

```python
a, b = 10, 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
```

## Comparison Operators

Comparison operators compare values and return boolean results (`True` or `False`).

- `==` Checks if values are equal.
- `!=` Checks if values are not equal.
- `>` Checks if the left value is greater.
- `<` Checks if the left value is smaller.
- `>=` Checks if the left value is greater than or equal.
- `<=` Checks if the left value is less than or equal.

```python
x, y = 5, 10
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to
```

## Boolean Operators

Boolean operators are used for logical operations.

- `and` Returns `True` if both conditions are true.
- `or` Returns `True` if at least one condition is true.
- `not` Reverses the boolean value.

```python
x, y = True, False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT
```

## String Concatenation

String concatenation joins multiple strings using the `+` operator.

```python
str1, str2 = "Hello", " World!"
result = str1 + str2
print(result)  # Output: Hello World!
```

## Ternary Operator

The ternary operator provides a concise way to write conditional statements.

Syntax: `value_if_true if condition else value_if_false`

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

Another example:

```python
meaning = 42
print('')

# Traditional if-else
# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not today')

# Ternary Operator
print('Right on!') if meaning > 10 else print('Not today')
```

## Rounding Function

### `round()`

The `round()` function rounds a floating-point number to a specified number of decimal places. If no number of decimals is specified, it rounds to the nearest integer.

```python
num = 4.56789
print(round(num, 2))  # Output: 4.57
print(round(num))     # Output: 5
```
