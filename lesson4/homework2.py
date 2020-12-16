from random import randint
x1 = []
def newfunc(start, finish):
    while start <= finish:
        yield randint(start, finish)
        start+=1
z = 0
for x in newfunc(1, 1213):
    if x > z:
        x1.append(x)
        z = x
    else:
        z = x
        continue
print(x1)



