# Python Scope

## Introduction

Scope in Python defines the accessibility of variables within different parts of a program. Understanding scope is essential to avoid unexpected behavior and errors.

Python has four types of scope, commonly referred to as **LEGB**:

1. **Local Scope**: Variables declared inside a function.
2. **Enclosing Scope**: Variables in the outer function of a nested function.
3. **Global Scope**: Variables declared at the top level of a script.
4. **Built-in Scope**: Variables that are built into Python (e.g., `print`, `len`).

---

## 1. Local Scope

A variable declared inside a function is accessible only within that function.

```python
def greeting():
    message = "Hello, World!"
    print(message)

greeting()
# print(message)  # This would raise an error because 'message' is not accessible outside the function
```

---

## 2. Enclosing Scope

Variables in the outer function of a nested function are accessible inside the inner function.

```python
def outer_function():
    outer_var = "I am from outer function"

    def inner_function():
        print(outer_var)  # Can access 'outer_var' from outer_function

    inner_function()

outer_function()
```

If we need to modify an enclosing variable inside the inner function, we use `nonlocal`:

```python
def outer():
    color = "blue"

    def inner():
        nonlocal color
        color = "red"  # Modifies the outer function's variable
        print("Inside inner:", color)

    inner()
    print("Inside outer:", color)

outer()
```

---

## 3. Global Scope

Variables declared at the top level of a script are accessible throughout the program.

```python
name = "Alice"  # Global variable

def greet():
    print("Hello", name)  # Can access 'name'

greet()
print(name)  # Accessible outside the function as well
```

If we need to modify a global variable inside a function, we use `global`:

```python
count = 0

def increment():
    global count  # Access and modify the global variable
    count += 1
    print("Count inside function:", count)

increment()
print("Count outside function:", count)
```

---

## 4. Built-in Scope

Python provides built-in functions that are accessible globally.

```python
print(len("Hello"))  # 'len' is a built-in function
```

Avoid overriding built-in names:

```python
# Bad practice
len = 10  # Overrides built-in 'len' function
# print(len("Hello"))  # This will raise an error
```

---

## Summary

| Scope Type | Description                                      | Keyword    |
| ---------- | ------------------------------------------------ | ---------- |
| Local      | Variable inside a function                       | None       |
| Enclosing  | Variable in outer function of a nested function  | `nonlocal` |
| Global     | Variable declared at the top level of the script | `global`   |
| Built-in   | Python’s built-in functions                      | None       |

Understanding scope ensures efficient variable usage and prevents unintended modifications in Python programs.
