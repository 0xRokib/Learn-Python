# Python Format Strings

Python provides multiple ways to format strings, making it easy to include variables in text dynamically. This guide covers different methods for formatting strings in Python.

## 1. Using `%` Formatting (Old Style)

The `%` operator is an older way to format strings in Python.

```python
person = "Rokib"
coins = 3

message = "%s has %s coins left." % (person, coins)
print(message)
```

### Pros:

- Simple and familiar to those with C experience.

### Cons:

- Can be difficult to read with multiple variables.
- Not as flexible as newer formatting methods.

## 2. Using `.format()` Method

Python introduced the `.format()` method to improve string formatting.

```python
message = "{} has {} coins left.".format(person, coins)
print(message)
```

You can also use positional or keyword arguments:

```python
message = "{1} has {0} coins left.".format(coins, person)
print(message)

message = "{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)
```

You can even pass a dictionary using `**`:

```python
player = {"person": "Rokib", "coins": 3}
message = "{person} has {coins} coins left.".format(**player)
print(message)
```

### Pros:

- More readable and flexible than `%` formatting.
- Allows named placeholders and reordering of variables.

### Cons:

- Slightly verbose compared to f-strings.

## 3. Using f-Strings (Best and Recommended)

Introduced in Python 3.6, f-strings (formatted string literals) provide the most readable and efficient way to format strings.

```python
message = f"{person} has {coins} coins left."
print(message)
```

f-Strings support expressions and methods directly within placeholders:

```python
message = f"{person.lower()} has {coins} coins left."
print(message)
```

f-Strings also work well with dictionaries:

```python
message = f"{player['person']} has {player['coins']} coins left."
print(message)
```

### Pros:

- Most readable and concise.
- Faster than `.format()` and `%` formatting.
- Allows inline expressions.

### Cons:

- Requires Python 3.6+.

## 4. Formatting Numbers with f-Strings

You can format numbers with precision:

```python
num = 10
print(f"2.25 times {num} is {2.25 * num:.2f}")
```

Looping with formatted numbers:

```python
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
```

Percentage formatting:

```python
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
```

## Conclusion

| Method         | Readability | Flexibility | Performance |
| -------------- | ----------- | ----------- | ----------- |
| `%` Formatting | Low         | Low         | Slow        |
| `.format()`    | Medium      | High        | Medium      |
| f-Strings      | High        | High        | Fast        |

f-Strings are the best choice for most use cases due to their readability, efficiency, and support for inline expressions. However, older methods like `%` formatting and `.format()` can still be useful in legacy code.

### Happy Coding! 🚀
