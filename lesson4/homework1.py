from sys import argv
def newfunc(salary, salary1, bonus):
    return ((salary*salary1)+bonus)
_, salary, salary1, bonus = argv
print(newfunc(float(salary), float(salary1), float(bonus)))

