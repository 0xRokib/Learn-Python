# Python Closure

## Introduction

A **closure** is a function object that retains access to variables from its enclosing lexical scope even when the function is called outside that scope.

Closures are useful for data encapsulation, maintaining state, and avoiding global variables.

---

## 1. Understanding Closures

A closure is created when:

1. A nested function references variables from its enclosing function.
2. The enclosing function returns the nested function.

Example:

```python
def parent_function(person, initial_coins):
    coins = initial_coins  # Local variable within the enclosing function

    def play_game():
        nonlocal coins  # Access and modify the enclosing variable
        if coins > 0:
            coins -= 1

        if coins > 1:
            print(f"\n{person} has {coins} coins left.")
        elif coins == 1:
            print(f"\n{person} has {coins} coin left.")
        else:
            print(f"\n{person} is out of game")

    return play_game

tommy = parent_function('Tommy', 3)
jenny = parent_function('Jenny', 5)

tommy()
tommy()
jenny()

tommy()
```

Here, `play_game` retains access to `coins` and `person` even after `parent_function` has finished executing.

---

## 2. Use Cases for Closures

Closures are commonly used in:

- **Function factories** (generating functions dynamically)
- **Encapsulating state**
- **Replacing classes for simple use cases**

Example of a function factory:

```python
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

by_two = multiplier(2)
by_three = multiplier(3)

print(by_two(5))  # Output: 10
print(by_three(5))  # Output: 15
```

---

## 3. Avoiding Common Pitfalls

- **Mutable default arguments** can lead to unexpected behavior.
- **Retaining references** instead of values can cause unintended side effects.

Example of an issue:

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = counter()
c2 = counter()

print(c1())  # Output: 1
print(c1())  # Output: 2
print(c2())  # Output: 1 (Separate instance)
```

---

## Summary

| Feature   | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| Closure   | A function that retains access to enclosing variables              |
| Use Cases | Function factories, encapsulating state, avoiding global variables |
| Keywords  | `nonlocal`, nested functions                                       |

Understanding closures allows you to write cleaner, more modular, and efficient Python code.
