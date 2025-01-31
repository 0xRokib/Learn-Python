# Python Lists and Tuples

## Introduction

Python provides two commonly used data structures: **lists** and **tuples**. Both store multiple items in a single variable, but they have key differences.

- **Lists** are mutable, meaning their contents can be changed after creation.
- **Tuples** are immutable, meaning they cannot be changed once created.

This document explains lists and tuples, along with a detailed breakdown of the provided code.

---

## Python List

A **list** is an ordered collection of elements that can be modified. Lists are defined using square brackets `[]`.

### List Features:

- Ordered (maintains the order of insertion)
- Mutable (can be modified after creation)
- Allows duplicate values
- Supports indexing and slicing

### Common List Operations:

```python
users = ['rokib', 'hasan', 'tani']  # Creating a list
```

#### 1. Checking for a Value in a List:

```python
print("rokib" in users)  # Returns True if 'rokib' exists in the list
```

#### 2. Retrieving List Values by Index:

```python
print(users[0])     # First element ('rokib')
print(users[-2])    # Second last element ('hasan')
print(users.index("rokib"))  # Index of 'rokib'
```

#### 3. Retrieving a Range of List Values (Slicing):

```python
print(users[0:2])   # ['rokib', 'hasan'] (elements from index 0 to 1)
print(users[1:])    # ['hasan', 'tani'] (elements from index 1 to end)
print(users[-3:-1]) # ['rokib', 'hasan'] (elements from index -3 to -2)
```

#### 4. Getting the Length of a List:

```python
print(len(users))  # Returns number of items in the list
```

#### 5. Adding Items to a List:

```python
users.append("elsa")               # Adds 'elsa' to the end
users += ['saki']                   # Adds 'saki' to the end
users.extend(['robert', 'jimmy'])    # Extends the list with multiple items
users.insert(0, 'Bob')               # Inserts 'Bob' at index 0
users[2:2] = ["Eddie", 'Alex']       # Inserts items at index 2
```

#### 6. Replacing List Values:

```python
users[1:3] = ["Robert", 'JPJ']  # Replaces values at index 1 and 2
```

#### 7. Removing, Deleting, and Clearing Items:

```python
users.remove("Bob")  # Removes 'Bob'
users.pop()         # Removes last element

# Deletes the first element in the list
# del data  # Uncomment to delete the entire list

data.clear()  # Clears all elements from 'data'
```

#### 8. Sorting Lists:

```python
users.sort()  # Sorts list in ascending order
users.sort(reverse=True)  # Sorts list in descending order
users.sort(key=str.lower)  # Case-insensitive sorting
```

#### 9. Copying a List:

```python
numscopy = nums.copy()  # Copies list using copy method
mynums = list(nums)     # Copies list using list() function
mycopy = nums[:]        # Copies list using slicing
```

#### 10. Sorting Numbers:

```python
nums = [4, 43, 75, 1, 5]
nums.sort()  # Sorts in ascending order
nums.sort(reverse=True)  # Sorts in descending order
print(sorted(nums))  # Returns a new sorted list without modifying original list
print(sorted(nums, reverse=True))  # Returns new list sorted in descending order
```

---

## Python Tuple

A **tuple** is an ordered, immutable collection of items. Tuples are defined using parentheses `()`.

### Tuple Features:

- Ordered (maintains the order of insertion)
- Immutable (cannot be changed after creation)
- Allows duplicate values
- Supports indexing and slicing

### Creating a Tuple:

```python
mytuple = tuple(('Dave', 42, 42, True))
anothertuple = (1, 23, 3, 45)
```

#### Converting Tuple to List and Modifying:

```python
newlist = list(mytuple)   # Convert tuple to list
newlist.append("Neil")    # Modify the list
newtuple = tuple(newlist)  # Convert back to tuple
```

#### Tuple Unpacking:

```python
(one, two, *hey) = anothertuple
print(one, two, hey)  # Output: 1 23 [3, 45]
```

#### Counting Occurrences in Tuple:

```python
print(newtuple.count(42))  # Counts occurrences of 42
```

---

## Summary

### Lists:

- Mutable (modifiable)
- Uses `[]`
- Supports various operations like append, insert, remove, and sort
- Used for collections that may change

### Tuples:

- Immutable (cannot be modified after creation)
- Uses `()`
- Faster than lists (due to immutability)
- Used for fixed collections of items

---

This document explains lists and tuples in Python and provides insights into the given code. Understanding these concepts is essential for efficient data handling in Python.
