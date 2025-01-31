#Dictionaries ans Sets

# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")

# Accessing Dictionary Items
print(band["vocals"])
print(band.get("guitar"))

# List all keys and values
print(band.keys())
print(band.values())
print(band.items())  # List key-value pairs as tuples

# Verify if a key exists
print("vocals" in band)
print("triangle" in band)

# Adding & Changing Values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Removing Items
print(band.pop("bass"))  # Remove and return the value
band["drums"] = "Bonham"
print(band.popitem())  # Remove and return the last key-value pair

del band["drums"]  # Delete a key-value pair

# Copying Dictionaries
band2 = band.copy()  # Creates an independent copy
print("Good Copy!")
band2["drums"] = "Rokib"
print(band2)

band3 = dict(band)  # Another way to copy a dictionary
print("Good Copy!")
print(band3)

# Nested Dictionaries
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}

my_band = {
    "member1": member1,
    "member2": member2
}
print(my_band)
print(my_band["member1"]["name"])

# Sets - No duplicates allowed
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(type(nums))
print(len(nums))

# True is a duplicate of 1, False is a duplicate of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value exists in a set
print(2 in nums)

# Add a new element to a set
nums.add(8)

# Update with multiple values
more_nums = {4, 5, 6}
nums.update(more_nums)
print(nums)

# Merge two sets
one = {1, 2, 3}
two = {4, 5, 6}
new_set = one.union(two)
print(new_set)

# Keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# Keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
