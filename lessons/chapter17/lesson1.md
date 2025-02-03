# Working with Files in Python

## 1. **Reading a File**

- Use `open(file_path, "r")` to open a file in read mode.
- If the file does not exist, a `FileNotFoundError` is raised.
- Use a `with` block to ensure the file is properly closed after reading.

```python
base_path = "code/chapter17/"
try:
    with open(f"{base_path}names.txt", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("The file 'names.txt' does not exist.")
```

---

## 2. **Appending to a File**

- Use `open(file_path, "a")` to open a file in append mode.
- If the file does not exist, it will be created.
- New content is added to the end of the file.

```python
base_path = "code/chapter17/"
with open(f"{base_path}names.txt", "a") as f:
    f.write("Neil\n")
```

---

## 3. **Writing to a File (Overwrite)**

- Use `open(file_path, "w")` to open a file in write mode.
- If the file exists, its content is overwritten. If it does not exist, it is created.

```python
base_path = "code/chapter17/"
with open(f"{base_path}context.txt", "w") as f:
    f.write("I deleted all of the context")
```

---

## 4. **Creating a File**

- Use `open(file_path, "w")` or `open(file_path, "x")` to create a file.
- The `"w"` mode creates or overwrites a file.
- The `"x"` mode creates a file but raises an error if the file already exists.

```python
base_path = "code/chapter17/"
# Using 'w' mode
with open(f"{base_path}name_list.txt", "w") as f:
    pass  # Creates an empty file

# Using 'x' mode
if not os.path.exists(f"{base_path}dave.txt"):
    with open(f"{base_path}dave.txt", "x") as f:
        pass  # Creates the file if it doesn't exist
else:
    print("The file 'dave.txt' already exists.")
```

---

## 5. **Deleting a File**

- Use `os.remove(file_path)` to delete a file.
- Check if the file exists using `os.path.exists(file_path)` before attempting to delete it.

```python
base_path = "code/chapter17/"
if os.path.exists(f"{base_path}dave.txt"):
    os.remove(f"{base_path}dave.txt")
    print("dave.txt deleted.")
else:
    print("The file 'dave.txt' does not exist.")
```

---

## 6. **Copying File Content**

- Read the content of one file and write it to another file using `"w"` mode.

```python
base_path = "code/chapter17/"
with open(f"{base_path}more_names.txt", "r") as source:
    content = source.read()

with open(f"{base_path}names.txt", "w") as destination:
    destination.write(content)
```

---

## Best Practices

- Always use the `with` statement when working with files to ensure they are properly closed after operations.
- Handle exceptions (e.g., `FileNotFoundError`) to make your code robust.
- Check for file existence before performing operations like deletion or creation in `"x"` mode.

---

## Example Directory Structure

```
code/
└── chapter17/
    ├── names.txt
    ├── context.txt
    ├── name_list.txt
    ├── dave.txt
    └── more_names.txt
```
