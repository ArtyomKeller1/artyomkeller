from itertools import count

newfile = open("homework2.txt", "a")
z = 0
list2 = "Two Five Six"
list2 = list2.split()
for x in list2:
    z+=1
newfile.write(f" ".join(list2) + str(z) + "\n")
z = 0
list1 = "One Six Five"
list1 = list1.split()
for x in list2:
    z+=1
newfile.write(" ".join(list1) + str(z) + "\n")
z = 0
list3 = "Zero Ten Six Five"
list3 = list3.split()
for x in list2:
    z+=1
newfile.write(" ".join(list3) + str(z) + "\n")






