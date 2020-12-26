class Matrix:
    def __init__(self, x, y, x1, y1):
        self.line = [[x, y], [x1, y1]]
    def __str__(self):
        return f"{self.line[0]}\n{self.line[1]}"
    def __add__(self, other):
        return f"{self.line[0][0] + other.line[0][0]} {self.line[0][1] + other.line[0][1]}\n{self.line[1][0] + other.line[1][0]} {self.line[1][1] + other.line[1][1]}"

matrix1 = Matrix(1, 2, 3, 4)
matrix2 = Matrix(2, 3, 5, 6)
print(matrix1+matrix2)

