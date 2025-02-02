# README: Python Command-Line Arguments

## Overview

Python command-line arguments let users pass input parameters to a script when executing it from the terminal or command prompt. This allows dynamic behavior without modifying the script code.

## What Are Command-Line Arguments?

Command-line arguments are values provided to a script when it is run from the command line. These arguments are accessible via the `sys.argv` list or the `argparse` module, which provides advanced parsing features.

## Why Use Command-Line Arguments?

- Enable users to input values dynamically without modifying the script.
- Facilitate automation by passing arguments via shell scripts or batch files.
- Support configurable behavior for scripts without hardcoded values.

## Handling Command-Line Arguments in Python

Python provides multiple ways to handle command-line arguments:

### Using `sys.argv`

`sys.argv` provides a simple way to access command-line arguments as a list.

```python
import sys

# sys.argv[0] is the script name
# sys.argv[1:] contains the arguments
print("Arguments passed:", sys.argv[1:])
```

Run:

```sh
python script.py arg1 arg2 arg3
```

Output:

```sh
Arguments passed: ['arg1', 'arg2', 'arg3']
```

### Using `argparse` (Recommended)

The `argparse` module provides a structured way to handle arguments.

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple example of command-line arguments.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--age", type=int, help="Your age")
    args = parser.parse_args()

    print(f"Hello {args.name}! You are {args.age} years old.")

if __name__ == "__main__":
    main()
```

Run:

```sh
python script.py Alice --age 30
```

Output:

```sh
Hello Alice! You are 30 years old.
```

## Features

- Uses `argparse` for handling command-line arguments.
- Supports greetings in English, Spanish, and German.
- Ensures input validation with required arguments and choices.
- Provides a user-friendly experience with clear descriptions and error handling.

## Prerequisites

Ensure Python (version 3.x recommended) is installed. Check your Python version by running:

```sh
python --version
```

## Usage

To run the script, use the following command:

```sh
python script.py -n <name> -l <language>
```

### Arguments

- `-n`, `--name`: Specifies the name of the person to greet (required).
- `-l`, `--lang`: Specifies the language of the greeting (required, choices: `English`, `Spanish`, `German`).

### Example Commands

```sh
python script.py -n Alice -l English
# Output: Hello Alice!

python script.py -n Bob -l Spanish
# Output: Hola Bob!

python script.py -n Charlie -l German
# Output: Hallo Charlie!
```

## Code Explanation

```python
import argparse  # Import argparse for command-line argument parsing

def hello(name, lang):
    """Function to print a personalized greeting."""
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"  # Corrected the German greeting
    }

    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(
        description="Provide a personal greeting."
    )

    # Add name argument
    parser.add_argument(
        "-n", "--name", metavar='name',
        required=True, help="The name of the person to greet"
    )

    # Add language argument with choices
    parser.add_argument(
        "-l", "--lang", metavar='language',
        required=True, choices=['English', "Spanish", "German"],
        help="The language of the greeting."
    )

    # Parse arguments
    args = parser.parse_args()

    # Call the function with parsed arguments
    hello(args.name, args.lang)
```

## Conclusion

This script demonstrates handling command-line arguments in Python, providing a structured and user-friendly way to interact with users via the terminal.

Happy Coding! 🚀
