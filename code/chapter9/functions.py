
# Simple function to print a message
def greet():
    print("Hello, welcome to Python functions!")
    
greet()

# Function with parameters and return value
def add_numbers(a, b):
    return a + b

result1 = add_numbers(5, 10)
result2 = add_numbers(20, 30)
print(result1)  # Output: 15
print(result2)  # Output: 50

# Function with default parameter value and type checking
def multiply(x, y=2):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Invalid input"
    return x * y

print(multiply(3, 4))  # Output: 12
print(multiply(5))     # Output: 10 (uses default y=2)
print(multiply("a", 3))  # Output: Invalid input

# Function accepting multiple positional arguments (*args)
def sum_all(*args):
    print(args)  # Output: tuple containing all arguments
    print(type(args))  # Output: <class 'tuple'>
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(10, 20))  # Output: 30

# Function accepting multiple keyword arguments (**kwargs)
def introduce(**kwargs):
    print(kwargs)  # Output: dictionary containing all keyword arguments
    print(type(kwargs))  # Output: <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

introduce(name="Alice", age=25, country="USA")


