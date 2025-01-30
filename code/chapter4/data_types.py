# Python Data Types

# String Data Type
first = 'Rokib'
last = "Hasan"

# String Constructor
pizza = str("Pepperoni")

# String Concatenation
fullname = first + " " + last + "!"
print(fullname)  # Output: Rokib Hasan!

# String Casting
decade = str(1998)

# Multi-line String
multiline = '''
Hey, hi! How are you?
I was just checking in.
                            All good?
'''
print(multiline)

# Escaping Special Characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at \\located?"
print(sentence)

# String Methods
print(first.lower())  # Lowercase
print(first.upper())  # Uppercase
print(multiline.title())  # Capitalize each word
print(multiline.replace('good', 'ok'))  # Replace words

# String Length & Stripping
print(len(multiline))  # Output: Length of string
print(multiline.strip())  # Removes leading and trailing spaces
print(multiline.lstrip())  # Removes leading spaces
print(multiline.rstrip())  # Removes trailing spaces

# Build a Menu
title = "MENU".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$3".rjust(4))
print("Cheesecake".ljust(16, '.') + "$5".rjust(4))

# String Indexing
print(first[1])  # Output: o
print(first[-1])  # Output: b
print(first[1:-1])  # Output: oki
print(first[1:])  # Output: okib
print(first[:])  # Output: Rokib

# Boolean Data Type
myvalue = True
x = bool(False)
print(type(x))  # Output: <class 'bool'>
print(isinstance(myvalue, bool))  # Output: True

# Numeric Data Types

# Integer Type
price = 100
best_price = int(80)
print(type(price))  # Output: <class 'int'>
print(isinstance(best_price, int))  # Output: True

# Float Type
gpa = 3.14
y = float(1.14)
print(type(gpa))  # Output: <class 'float'>
print(isinstance(y, float))  # Output: True

# Complex Type
comp_value = 5 + 3j
print(type(comp_value))  # Output: <class 'complex'>
print(comp_value.real)  # Output: 5.0
print(comp_value.imag)  # Output: 3.0

# Built-in Functions for Numbers
print(abs(gpa))  # Absolute value
print(abs(gpa * -1))  # Convert to positive
print(round(gpa))  # Round off
print(round(gpa, 1))  # Round with precision

# Math Operations
import math

print(math.pi)  # Pi value
print(math.sqrt(64))  # Square root
print(math.ceil(gpa))  # Ceiling value
print(math.floor(gpa))  # Floor value

# Casting String to Number
zipcode = '1001'
zip_value = int(zipcode)
print(type(zip_value))  # Output: <class 'int'>
