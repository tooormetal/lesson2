a = [[3, 6, 5], [4, 7, 5], [8, 3, 3]]
b = [[5, 7, 1], [0, 0, 9], [2, 5, 6]]

class Matrix:
    def __init__(self, matr):
        self.matr = matr
    def __str__(self):
        return '\n'.join(map(str, self.matr))
    def __add__(self, other):
        c = []
        for i in range(len(self.matr)):
            c.append([])
            for n in range(len(self.matr[0])):
                c[i].append(self.matr[i][n] + other.matr[i][n])
        return '\n'.join(map(str,c))
matrix1 = Matrix(a)
matrix2 = Matrix(b)
print(matrix1 + matrix2)
