a = input()
b = input()
c = input()
d = input()
y = input()
list1 = [a, b, c, d]
list2 = [a, b, c, d, y]
list1[0], list1[1] = list1[1], list1[0]
list1[2], list1[3] = list1[3], list1[2]
print(list1)
list2[0], list2[1] = list2[1], list2[0]
list2[2], list2[3] = list2[3], list2[2]
print(list2)



