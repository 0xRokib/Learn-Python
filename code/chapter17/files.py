import os

# Define the base path
base_path = "code/chapter17/"

# Read: Opens a file for reading, raises error if it doesn't exist
try:
    with open(f"{base_path}names.txt", "r") as f:
        # Iterate over each line in the file and print it
        for line in f:
            print(line)

except FileNotFoundError:
    print("The file 'names.txt' does not exist.")

# Append: Opens a file for appending, creates it if it doesn't exist
with open(f"{base_path}names.txt", "a") as f:
    f.write("Neil\n")

# Read the content after appending to verify
with open(f"{base_path}names.txt", "r") as f:
    print(f.read())

# Write (overwrite): Opens a file for writing, overwrites the existing content
with open(f"{base_path}context.txt", "w") as f:
    f.write("I deleted all of the context")

# Read the content to verify it has been overwritten
with open(f"{base_path}context.txt", "r") as f:
    print(f.read())

# Create a file using 'w' mode (overwrite if exists, or create if not)
with open(f"{base_path}name_list.txt", "w") as f:
    pass  # File is created and closed immediately

# Create a file using 'x' mode (fails if file exists)
if not os.path.exists(f"{base_path}dave.txt"):
    with open(f"{base_path}dave.txt", "x") as f:
        pass  # File is created
else:
    print("The file 'dave.txt' already exists.")

# Delete a file: Check if it exists before deleting
if os.path.exists(f"{base_path}dave.txt"):
    os.remove(f"{base_path}dave.txt")
    print("dave.txt deleted.")
else:
    print("The file 'dave.txt' does not exist.")

# Using 'with' for file handling ensures that files are automatically closed
with open(f"{base_path}more_names.txt", "r") as f:
    content = f.read()

# Writing the content of 'more_names.txt' to 'names.txt'
with open(f"{base_path}names.txt", "w") as f:
    f.write(content)
