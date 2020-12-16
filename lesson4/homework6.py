from itertools import count
from itertools import cycle

x = 0
x1 = []
for el in count(1):
    if el == 10:
        break
    else:
        x1.append(el)
for y in cycle(x1):
    if x == 10:
        break
    else:
        print(y)
    x += 1