# Python Basics

## 1. Variables in Python

A **variable** is a named storage for data in Python.

### Example from the given code:

```python
line01 = "********************"  # header/footer
line02 = "*                  *"  # re-use
line03 = "*     WELCOME!     *"
```

Here, `line01`, `line02`, and `line03` store string values.

## 2. Variable Naming Convention

Follow these best practices when naming variables:

- Use descriptive names.
- Use lowercase letters with underscores (snake_case).
- Avoid Python keywords as variable names.
- Start with a letter or underscore, not a number.

**Examples:**

```python
valid_variable = "Hello"
_valid_variable = "World"
```

## 3. Expressions vs Statements

- **Expression**: Code that evaluates to a value.
- **Statement**: A complete instruction performing an action.

### Example:

```python
line01 = "********************"  # Assignment statement
print(line01)  # Print statement
```

- `"********************"` is an **expression**.
- The assignment and `print()` calls are **statements**.

## 4. Comments in Python

Comments start with `#` and are ignored during execution. They explain the code.

### Example:

```python
# Print a blank line
print('')
```

## 5. Indentation in Python

Python uses indentation to define blocks of code.

### Example:

```python
if True:
    print("This is indented correctly")
```

Incorrect indentation causes an error:

```python
if True:
print("This will cause an error")
```
