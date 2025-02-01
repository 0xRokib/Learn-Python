# Python Recursion

## Introduction

Recursion is a programming technique where a function calls itself to solve a problem. It is useful for breaking down complex problems into smaller, more manageable parts. In Python, recursion can be used to solve problems that can be expressed in terms of smaller subproblems of the same type.

## How Recursion Works

A recursive function must have:

1. **Base Case**: A condition to stop the recursion.
2. **Recursive Case**: The function calls itself with a modified argument.

### Example: Simple Recursion

```python
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

_In this example, the function prints numbers from `n` down to 1 and stops when `n <= 0` (the base case)._

## Example: Recursive Function to Add One Until a Condition is Met

```python
def add_one(num):
    if num >= 9:  # Base case
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)  # Recursive call

mynewtotal = add_one(0)
print(mynewtotal)
```

_This function keeps adding one to `num` and calls itself recursively until `num` reaches 9, then it returns `num + 1`._

## Recursive vs. Iterative Approach

Recursive functions can be elegant but may lead to stack overflow if not handled properly. Iterative solutions, using loops, are generally more memory-efficient.

### Example: Factorial Using Recursion vs Iteration

**Recursive Approach:**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

**Iterative Approach:**

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # Output: 120
```

## Best Practices for Recursion

- **Define a clear base case** to prevent infinite recursion.
- **Limit recursion depth** since Python has a recursion limit (default is 1000 calls).
- **Use memoization (caching)** to optimize performance in functions like Fibonacci sequence.
- **Consider an iterative solution** if recursion is not necessary.

## Conclusion

Recursion is a powerful tool for solving problems that involve repetitive subproblems. However, it should be used cautiously, keeping efficiency and stack limitations in mind.
