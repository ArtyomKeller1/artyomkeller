def count():
    y = []
    while 1 < 10:
        stroka = input()
        strokaint = stroka.split()
        z = 0
        for x in strokaint:
            try:
                x = int(x)
            except ValueError:
                break
            z += x
        y.append(z)
        print(sum(y))
count()



