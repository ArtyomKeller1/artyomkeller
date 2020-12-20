nf = open("homework5.txt", "w")
nf.writelines(input())
nf.close()
nf1 = open("homework5.txt", "r")
a = nf1.readline()
a1 = a.split()
print(a1)
l1 = []
for x in a1:
    x = int(x)
    l1.append(x)
print(sum(l1))

