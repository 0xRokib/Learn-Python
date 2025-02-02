# Python Module System and Import Mechanisms

## 1. Built-in Modules

Python comes with a set of built-in modules that provide useful functionalities. These modules can be imported using the `import` statement.

### Example:

```python
from math import pi
import sys
import random as rdm

print(f"Value of pi: {pi}")
```

The `math` module is a built-in module that provides mathematical functions, including the value of π.

## 2. Custom Modules

A custom module is a Python file (`.py`) containing functions, variables, and classes that can be imported into another Python script.

### Example:

**modules.py:**

```python
from math import pi
import sys
import random as rdm
import kansas  # Importing the custom kansas module

print(f"Value of pi: {pi}")

print(f"Random choice: {rdm.choice('123')}")

# Accessing variables from the kansas module
print(f"Kansas Capital: {kansas.capital}")

# Calling the function from kansas module
kansas.randomfunfact()

# Checking the special __name__ variable
print(f"__name__ in modules.py: {type(__name__)}")

# Printing the __name__ attribute of the imported kansas module
print(f"__name__ in kansas module: {kansas.__name__}")
```

**kansas.py:**

```python
from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")
    print(f"Fun Fact: {funfacts[int(index)]}")

if __name__ == "__main__":
    print("Executing kansas.py directly:")
    randomfunfact()
```

## 3. Different Import Styles

Python supports different ways to import modules:

### a) Import the entire module:

```python
import random
print(random.choice([1, 2, 3]))
```

### b) Import specific functions or variables:

```python
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793
```

### c) Import with an alias:

```python
import random as rdm
print(rdm.choice([1, 2, 3]))
```

### d) Import all names (not recommended):

```python
from math import *
print(sin(pi / 2))  # Output: 1.0
```

_Note:_ This can lead to conflicts if multiple modules define functions with the same name.

## 4. Understanding `__name__ == "__main__"`

The `__name__` variable determines whether a script is run directly or imported as a module.

### Example:

**modules.py:**

```python
if __name__ == "__main__":
    print("modules.py is run directly.")
else:
    print("modules.py has been imported.")
```

**Running modules.py directly:**

```
$ python modules.py
modules.py is run directly.
```

**Importing it into another script (kansas.py):**

```python
import modules
```

**Output:**

```
modules.py has been imported.
```

### Why use `__name__ == "__main__"`?

- When a script is executed directly, `__name__` is set to `"__main__"`.
- When imported, `__name__` is set to the module's name.
- This allows separating script execution from module functionality.

## Conclusion

- Python modules help in organizing code.
- Importing allows using built-in and custom modules.
- Different import methods offer flexibility in accessing module content.
- The `__name__ == "__main__"` check helps in distinguishing between direct execution and module import.
