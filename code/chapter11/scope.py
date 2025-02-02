# global scope 
# name = "Rokib"
# def greeting(name):
#     color = 'blue'
#     print(color)
#     print(name)
    
# greeting('John')

count = 1
def another():
    color = 'blue'
    global count
    count += 1
    def greeting(name):
        nonlocal color
        color = 'red'
        print(color)
        print(name)
        
    greeting("dave")
    
another()