def int_func(x):
    print(x.capitalize())


def int_func1(x):
    emptylist=[]
    x1 = x.split()
    for y in x1:
        y = y.capitalize()
        emptylist.append(y)
    print(" ".join(emptylist))





