from random import randint
x1 = []
x2 = []
z = 0
def newfunc(start, finish):
    while start <= finish:
        yield randint(start, finish)
        start+=1
for x in newfunc(1, 2313):
     x1.append(x)
for i in x1:
    if i not in x2:
        x2.append(i)
print(x2)

