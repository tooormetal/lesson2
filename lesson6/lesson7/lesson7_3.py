class Cell:
    def __init__(self, param):
        self.param = param
    def __str__(self):
        return self.param
    def __add__(self, other):
        return self.param + other.param
    def __sub__(self, other):
        if self.param > other.param:
            return self.param - other.param
        else:
            return "вычитание невозможно"
    def __mul__(self, other):
        return self.param * other.param
    def __floordiv__(self, other):
        return self.param // other.param
    def make_order(self, number):
        return "\n".join(['*' * number for i in range(self.param // number)]) + "\n" + '*' * (self.param % number)

cell1 = Cell(15)
cell2 = Cell(23)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1.make_order(4))
