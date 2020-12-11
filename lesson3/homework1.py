def division():
    a = int(input())
    b = int(input())
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Деление на ноль")
division()
