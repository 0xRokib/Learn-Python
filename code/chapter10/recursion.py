def add_one(num):
    if num >= 9:  # Base case
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)  # Recursive call

mynewtotal = add_one(0)
print(mynewtotal)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120



def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # Output: 120