class Cell:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x
    def __sub__(self, other):
        return self.x - other.x
    def __mul__(self, other):
        return self.x * other.x
    def __truediv__(self, other):
        return self.x // other.x
    def make_order(self):
        a = self.x // 5
        b = self.x % 5
        return (("*"*5 + "\n") * a) + "*"*b
c = Cell(12)
c1 = Cell(5)
print(c+c1)
print(c-c1)
print(c*c1)
print(c/c1)
print(c.make_order())