from functools import reduce

x = [el for el in range(100, 1001)]
def multiply(a, b):
    return a*b
print(reduce(multiply, x))