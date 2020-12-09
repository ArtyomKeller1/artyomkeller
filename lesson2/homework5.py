y = 0
while y < 10:
    numbers = [7, 5, 3, 3, 2]
    x1 = len(numbers)
    x = int(input())
    if x in numbers:
        el_index = numbers.index(x)
        numbers.insert(el_index, x)
        numbers.sort()
        numbers.reverse()
        print(numbers)
    else:
        numbers.append(x)
        numbers.sort()
        numbers.reverse()
        print(numbers)


