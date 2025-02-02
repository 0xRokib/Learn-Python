# Global Scope
global_var = "I am global"

def outer_function():
    # Enclosing Scope
    enclosing_var = "I am enclosing"

    def inner_function():
        # Local Scope
        local_var = "I am local"
        print(local_var)  # Accessing local variable
        print(enclosing_var)  # Accessing enclosing variable
        print(global_var)  # Accessing global variable
    
    inner_function()

outer_function()

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1
    print("Counter:", counter)

increment()
increment()

# Using nonlocal
def outer():
    enclosing_value = "blue"

    def inner():
        nonlocal enclosing_value
        enclosing_value = "red"
        print("Inside inner:", enclosing_value)

    inner()
    print("Inside outer:", enclosing_value)

outer()
