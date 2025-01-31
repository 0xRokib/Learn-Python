# Python list and tuple 

# Lists
users = ['rokib', 'hasan', 'tani']
data = ['rokib, 42, true']
empty_list = []

# Check for a value in a list
print("rokib" in users)

# Retrieve a list value by index
print(users[0])
print(users[-2])
print(users.index("rokib"))

# Retrieve a range of list values
print(users[:2])
print(users[1:])
print(users[-3:-1])

# Get the length of a list
print(len(data))

# Modifying lists
users.append("elsa")
users += ['saki']
users.extend(['robert', 'jimmy'])
users.extend(data)
users.insert(0, 'Bob')
users[2:2] = ["Eddie", 'Alex']
users[1:3] = ["Robert", 'JPJ']

# Removing elements
users.remove("Bob")
users.pop()
del users[0]
data.clear()

# Sorting lists
users[1:2] = ['dave']  # Adding a lowercase item
users.sort()
# users.sort(key=str.lower)  # Case-insensitive sorting

# Working with numbers
nums = [4, 43, 75, 1, 5]
nums.reverse()
# nums.sort(reverse=True)  # Sort in descending order

# Copying lists
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(type(nums))
mylist = list([1, 2, 34, 7])

# Tuples
mytuple = ('Dave', 42, 42, True)
anothertuple = (1, 23, 3, 45)

# Convert tuple to list, modify, and convert back
temp_list = list(mytuple)
temp_list.append("Neil")
newtuple = tuple(temp_list)

# Unpacking tuples
one, two, *rest = anothertuple
print(one, two, rest)
print(newtuple.count(42))
