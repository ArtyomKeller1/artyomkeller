a = input()
y = a.split()
z = 1
for x in y:
    if len(x) > 10:
        b = list(x)
        p = "".join(b[0:10])
        print(z, p)
        z += 1
        continue
    else:
        print(z, x)
        z += 1