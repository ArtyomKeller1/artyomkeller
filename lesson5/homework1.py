f_open = open("homework1.txt", "a")
a = input()
while a != "":
    f_open.write(a)
    f_open.write("\n")
    a = input()
f_open.close()