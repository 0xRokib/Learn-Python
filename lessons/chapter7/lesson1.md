# Python Dictionaries and Sets

## Dictionaries

A dictionary in Python is an unordered, mutable collection that stores key-value pairs. It allows quick lookups and modifications.

### Creating Dictionaries

Dictionaries can be created using curly braces `{}` or the `dict()` constructor.

```python
band = {
    'vocals': "Plant",
    'guitar': "Page"
}

band2 = dict(vocals="Plant", guitar='Page')
```

### Accessing Dictionary Items

Dictionary values can be accessed using keys.

```python
print(band['vocals'])  # Output: Plant
print(band.get("guitar"))  # Output: Page
```

### Listing Keys, Values, and Items

```python
print(band.keys())  # Returns all keys
print(band.values())  # Returns all values
print(band.items())  # Returns key-value pairs as tuples
```

### Checking Key Existence

```python
print("vocals" in band)  # True
print("triangle" in band)  # False
```

### Adding & Modifying Items

```python
band['vocals'] = 'Coverdale'  # Modifying an existing value
band.update({"bass": "JPJ"})  # Adding a new key-value pair
```

### Removing Items

```python
print(band.pop('bass'))  # Removes and returns value
band['drums'] = 'Bonham'
print(band.popitem())  # Removes and returns the last inserted key-value pair

band['drums'] = 'Bonham'
del band['drums']  # Deletes a specific key
```

### Clearing and Deleting Dictionaries

```python
band2.clear()  # Clears the dictionary
print(band2)  # Output: {}
del band2  # Deletes the dictionary
```

### Copying Dictionaries

Assigning a dictionary to a new variable creates a reference, not a copy.

```python
band2 = band.copy()  # Creates an independent copy
band2['drums'] = 'Rokib'
print(band2)
```

Alternative way:

```python
band3 = dict(band)
print(band3)
```

### Nested Dictionaries

Dictionaries can contain other dictionaries.

```python
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}

my_band = {
    "member1": member1,
    "member2": member2
}
print(my_band["member1"]["name"])  # Output: Plant
```

## Sets

A set is an unordered collection of unique elements.

### Creating Sets

```python
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
```

### Checking Membership

```python
print(2 in nums)  # True
```

### Unique Elements

Sets do not allow duplicate values. `True` is considered as `1`, and `False` as `0`.

```python
nums = {1, True, 2, False, 3, 4, 0}
print(nums)  # Output: {False, True, 2, 3, 4}
```

### Adding Elements

```python
nums.add(8)
```

### Updating a Set

```python
morenums = {4, 5, 6}
nums.update(morenums)
print(nums)
```

### Merging Sets

```python
one = {1, 2, 3}
two = {4, 5, 6}
newset = one.union(two)
print(newset)
```

### Finding Common Elements

```python
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)  # Output: {2, 3}
```

### Finding Unique Elements

```python
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)  # Output: {1, 4}
```

## Conclusion

- **Dictionaries** are key-value stores allowing fast lookups, updates, and nested data.
- **Sets** store unique items and support mathematical operations like unions and intersections.
- Both structures enhance Python’s data-handling capabilities and are widely used in real-world applications.
