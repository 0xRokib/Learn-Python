# Python Data Types

## Introduction

Python provides several built-in data types to store and manipulate different kinds of data. Understanding these data types is crucial for effective programming in Python.

---

## 1. String Data Type

Strings in Python are sequences of characters enclosed in single (`'`), double (`"`), or triple quotes (`'''` or """").

### Declaration:

```python
first = 'Rokib'
last = "Hasan"
```

### String Constructor:

```python
pizza = str("Pepperoni")
```

### String Concatenation:

```python
fullname = first + " " + last
fullname += '!'
print(fullname)  # Output: Rokib Hasan!
```

### Type Checking:

```python
print(type(first))  # Output: <class 'str'>
print(isinstance(first, str))  # Output: True
```

### Multi-line String:

```python
multiline = '''
Hey, hi! How are you?
I was just checking in.
                All good?
'''
print(multiline)
```

### Escaping Special Characters:

```python
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located?'
print(sentence)
```

### String Methods:

```python
print(first.lower())  # Output: rokib
print(first.upper())  # Output: ROKIB
print(multiline.title())  # Capitalizes each word
print(multiline.replace('good', 'ok'))  # Replace words
```

### String Length & Stripping:

```python
print(len(multiline))  # Output: Length of string
print(multiline.strip())  # Removes leading and trailing spaces
```

### String Indexing:

```python
print(first[1])  # Output: o
print(first[-1])  # Output: b
print(first[1:-1])  # Output: oki
print(first[1:])  # Output: okib
print(first[:])  # Output: Rokib
```

### Checking Start & End of String:

```python
print(first.startswith("R"))  # Output: True
print(first.endswith("b"))  # Output: True
```

---

## 2. Boolean Data Type

Boolean values represent `True` or `False`.

```python
myvalue = True
x = bool(False)
print(type(x))  # Output: <class 'bool'>
print(isinstance(myvalue, bool))  # Output: True
```

---

## 3. Numeric Data Types

### Integer (`int`)

```python
price = 100
best_price = int(80)
print(type(price))  # Output: <class 'int'>
print(isinstance(best_price, int))  # Output: True
```

### Float (`float`)

```python
gpa = 3.14
y = float(1.14)
print(type(gpa))  # Output: <class 'float'>
print(isinstance(y, float))  # Output: True
```

### Complex Numbers (`complex`)

```python
comp_value = 5 + 3j
print(type(comp_value))  # Output: <class 'complex'>
print(comp_value.real)  # Output: 5.0
print(comp_value.imag)  # Output: 3.0
```

### Built-in Functions for Numbers

```python
print(abs(gpa))  # Output: 3.14
print(abs(gpa * -1))  # Output: 3.14
print(round(gpa))  # Output: 3
print(round(gpa, 1))  # Output: 3.1
```

### Mathematical Operations Using `math` Module

```python
import math
print(math.pi)  # Output: 3.141592653589793
print(math.sqrt(64))  # Output: 8.0
print(math.ceil(gpa))  # Output: 4
print(math.floor(gpa))  # Output: 3
```

### Casting Strings to Numbers

```python
zipcode = '1001'
zip_value = int(zipcode)
print(type(zip_value))  # Output: <class 'int'>
```

---

## Conclusion

Python provides various data types, including strings, booleans, and numeric types (int, float, complex). Understanding these data types and their operations helps in writing efficient and error-free code.
