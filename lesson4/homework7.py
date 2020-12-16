import math
def fact(n):
    a = range(1, n+1)
    for i in a:
        yield math.factorial(i)
for el in fact(10):
    print(el)

