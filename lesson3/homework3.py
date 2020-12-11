def my_func():
    a = int(input())
    b = int(input())
    d = int(input())
    newlist = [a, b, d]
    newlist.sort()
    print(newlist[-1]+newlist[-2])
my_func()