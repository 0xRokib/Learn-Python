# Basic While Loop
# value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))


# for loop 
# names = ['Rokib','Sarah','John']
# for name in names:
#     print(name)
    
# looping string 
# for ch in "Rokib":
#     print(ch)
    
#break with fo loop
# names = ['Rokib','Sarah','John']
# for name in names:
#     if name == "Sarah":
#         break
#     print(name)

# continue with for 
# names = ['Rokib','Sarah','John']
# for name in names:
#     if name == "Sarah":
#         continue
#     print(name)
    
# for loop with range 
# for i in range(5):
#     print(i)
    
# for x in range(2,5):
#     print(x)

# for x in range(5,101,5):
#     print(x)
# else:
#     print("Glad That's over!")


# nested loop 
names = ['rokib','hasan','tani']
actions = ['codes','eats','sleeps']

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")