users = ['rokib','hasan','tani']
data = ['rokib, 42, true']
emptylist = []

# Check for a value in a list
print("rokib" in users)


#Retrieve a list value by index
print(users[0])
print(users[-2])
print(users.index("rokib"))

# Retrieve a range of list values
print(users[0:2])
print(users[1:])
print(users[-3:-1])

# Get the length of a list
print(len(data))

# Appending items to a list
users.append("elsa")
users += ['saki']
users.extend(['robert','jimmy'])
users.extend(data)
users.insert(0, 'Bob')
users[2:2] = ["Eddie", 'Alex']

# Replacing list values
users[1:3] = ["Robert",'JPJ']

# Removing, deleting, clearing
users.remove("Bob")
users.pop()
del users[0]
# del data # delete entire list
data.clear() #delete entry from list and make it empty


# Sorting lists
users[1:2] = ['dave'] #adding lower case item 
users.sort()
# users.sort(key=str.lower)
# print(users)

nums = [4,43,75,1,5]
nums.reverse()
# nums.sort(reverse=True)
# print(nums)
# print(sorted(nums, reverse=True))
# print(nums)

# copy 
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

# print(numscopy)
# print(mynums)
# print(mycopy)
# print(nums)

print(type(nums))
mylist = list([1,2,34,7])
# print(mylist)



# tuple 

mytuple = tuple(('Dave', 42, 42, True))
anothertuple = (1,23,3,45,)
# print(type(tuple))
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
# print(newtuple)

# unpack tuple 
(one, two , *hey) = anothertuple
print(one, two, hey)
print(newtuple.count(42)) # how many times the number is present there
