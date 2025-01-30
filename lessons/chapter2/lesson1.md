# Setting Up Python with VS Code

This guide will help you set up Python in Visual Studio Code (VS Code) and run a simple "Hello, World!" program.

## Prerequisites

Make sure you have the following installed:

1. **[Python](https://www.python.org/downloads/)** (Ensure you check "Add Python to PATH" during installation)
2. **[Visual Studio Code](https://code.visualstudio.com/Download)**
3. **Python Extension for VS Code** (Install via the Extensions Marketplace)

## Step 1: Verify Python Installation

After installing Python, open a terminal (Command Prompt, PowerShell, or macOS/Linux terminal) and run:

```sh
python --version
```

or

```sh
python3 --version
```

You should see an output like `Python 3.x.x`. If not, check your installation.

## Step 2: Install Python Extension in VS Code

1. Open VS Code
2. Go to **Extensions** (`Ctrl+Shift+X` / `Cmd+Shift+X` on Mac)
3. Search for **Python** and install the one from Microsoft

## Step 3: Create a Python File

1. Open a folder in VS Code where you want to create your project.
2. Create a new file called `hello.py`.
3. Add the following code:

```python
print("Hello, World!")
```

## Step 4: Run the Python Script

### Using the VS Code Terminal

1. Open the terminal in VS Code (` Ctrl+`` / Cmd+`` on Mac `)
2. Navigate to the directory containing `hello.py` (if not already there)
3. Run the script using:

   ```sh
   python hello.py
   ```

   or

   ```sh
   python3 hello.py
   ```

### Using the VS Code Run Button

1. Click the **Run** button at the top right or press `F5`
2. Select "Python File" as the environment if prompted.
3. You should see `Hello, World!` printed in the terminal.

## Step 5: Set Up Virtual Environment (Optional, but Recommended)

To manage dependencies effectively, set up a virtual environment:

```sh
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

Now, you can install dependencies inside this environment using `pip install <package>`.

## Conclusion

You have successfully set up Python in VS Code and run a simple script! 🎉

For more, check out the [official VS Code Python documentation](https://code.visualstudio.com/docs/python/python-tutorial).
