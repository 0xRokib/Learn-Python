# Python Virtual Environment & Package Management with pip

## Introduction

A Python virtual environment allows you to create an isolated workspace for your Python projects, ensuring that dependencies do not conflict between different projects. The `pip` package manager is used to install and manage Python packages within these environments.

## Prerequisites

Ensure that Python is installed on your system. You can check by running:

```sh
python --version
```

OR

```sh
python3 --version
```

## Creating and Using a Virtual Environment

### 1. Creating a Virtual Environment

To create a virtual environment, use the following command:

```sh
python -m venv myenv
```

OR

```sh
python3 -m venv myenv
```

This creates a directory `myenv/` containing the isolated environment.

### 2. Activating the Virtual Environment

- **Windows (CMD/PowerShell)**:

  ```sh
  myenv\Scripts\activate
  ```

  OR

  ```sh
  myenv\Scripts\activate.bat  # CMD
  myenv\Scripts\Activate.ps1   # PowerShell
  ```

- **Mac/Linux**:
  ```sh
  source myenv/bin/activate
  ```

After activation, your terminal will show the virtual environment name as a prefix.

### 3. Deactivating the Virtual Environment

To exit the virtual environment, simply run:

```sh
deactivate
```

## Managing Packages with pip

### 1. Installing a Package

Use `pip` to install packages:

```sh
pip install package_name
```

Example:

```sh
pip install requests
```

### 2. Listing Installed Packages

To see a list of installed packages:

```sh
pip list
```

### 3. Freezing Dependencies

To save installed dependencies to a file:

```sh
pip freeze > requirements.txt
```

### 4. Installing Dependencies from a File

To install dependencies from `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 5. Uninstalling a Package

```sh
pip uninstall package_name
```

Example:

```sh
pip uninstall requests
```

## Example Python Script in a Virtual Environment

After setting up your virtual environment and installing packages, you can create and run a Python script:

1. Create a script `app.py`:

```python
import requests

response = requests.get('https://api.github.com')
print(response.json())
```

2. Run the script inside the virtual environment:

```sh
python app.py
```

## Removing a Virtual Environment

Simply delete the `myenv/` directory:

```sh
rm -rf myenv  # Mac/Linux
rd /s /q myenv  # Windows (CMD)
```

## Conclusion

Using virtual environments ensures clean project dependencies, and `pip` helps manage packages efficiently. Happy coding!

---
