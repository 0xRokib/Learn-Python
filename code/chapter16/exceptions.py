# 1. Basic Try-Except
# This block handles a ZeroDivisionError.
print("Basic Try-Except Example:")
x = 10
y = 0

try:
    result = x / y  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")  # Handle the exception here
finally:
    print("This will always print.\n")  # The finally block will execute regardless

# 2. Handling Multiple Exceptions
# This block demonstrates handling different types of errors (ZeroDivisionError, TypeError).
print("Handling Multiple Exceptions Example:")
x = "Hello"
y = 5

try:
    result = x + y  # This will cause a TypeError since you can't add a string and a number
except ZeroDivisionError:
    print("You can't divide by zero!")  # Handle ZeroDivisionError
except TypeError:
    print("You can't add a string and a number!")  # Handle TypeError
except Exception as e:
    print(f"An error occurred: {e}")  # This will catch any other exception that wasn't explicitly handled
finally:
    print("This will always print.\n")  # This will always run after the try-except blocks

# 3. Using Else Block (No Errors)
# This block demonstrates how the 'else' block is used when no exception is raised in the try block.
print("Using Else Block Example:")
x = 10
y = 2

try:
    result = x / y  # This will not cause any error (no division by zero)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is: {result}")  # This will run if no exception occurs
finally:
    print("This will always print.\n")

# 4. Using Finally Block
# The 'finally' block will always run, regardless of whether there was an exception or not.
print("Using Finally Block Example:")
x = 10
y = 0

try:
    result = x / y  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")  # Handle the exception here
finally:
    print("This will always print.\n")  # The finally block will execute whether or not there was an exception

# 5. Raising Exceptions
# Sometimes, you want to manually raise an exception.
print("Raising Exceptions Example:")
x = -1

try:
    if x < 0:
        raise ValueError("x cannot be negative!")  # Raising a ValueError with a custom message
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("This will always print.\n")

# 6. Custom Exception Types (without using classes)
# In Python, we can raise built-in exceptions with custom messages or use custom error types directly.
print("Custom Exception (Built-in with Custom Message):")
def process_data(data):
    if not isinstance(data, str):
        raise TypeError("Only strings are allowed!")  # Raise a TypeError with a custom message

try:
    process_data(42)  # Passing an invalid type (integer instead of string)
except TypeError as e:
    print(f"Error: {e}")
finally:
    print("This will always print.\n")

# 7. Catching Multiple Exceptions in One Line
# This shows how to catch multiple exceptions in one `except` block.
print("Catching Multiple Exceptions in One Line Example:")
x = "Hello"
y = 0

try:
    result = x / y  # This will cause both a TypeError and a ZeroDivisionError
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")
finally:
    print("This will always print.\n")

# 8. Asserting Conditions with `assert` (Optional Error Raising)
# The `assert` statement helps raise exceptions if a condition is not true.
print("Using Assert Example:")
def check_positive(number):
    assert number > 0, "Number must be positive!"  # Assert that the number is positive

try:
    check_positive(-5)  # This will raise an AssertionError because -5 is not positive
except AssertionError as e:
    print(f"Assertion Error: {e}")
finally:
    print("This will always print.\n")

# 9. Catching All Exceptions (Not Recommended)
# This is a bad practice but sometimes used when you want to catch any and all exceptions.
print("Catching All Exceptions Example:")
x = "Hello"
y = 0

try:
    result = x / y  # This will cause a TypeError
except Exception as e:  # Catching all exceptions (generic)
    print(f"An error occurred: {e}")
finally:
    print("This will always print.\n")
