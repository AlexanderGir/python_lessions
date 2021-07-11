#1
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mat = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
        for i in range(len(self.list_1)):
            for a in range(len(self.list_2[i])):
                mat[i][a] = self.list_1[i][a] + self.list_2[i][a]
        return str('\n'.join(['\t'.join([str(a) for a in i]) for i in mat]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(a) for a in i]) for i in mat]))

matrix = Matrix([[10, 7, 6],
                [8, 19, 13],
                [33, 44, 7]],
                [[42, 5, 2],
                [7, 7, 66],
                [22, 55, 66]])

print(matrix.__add__())

#2
class Сlothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь ткани (общая): {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани пальто {self.square_c}'

class Jacket(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани костюма {self.square_j}'


coat_1 = Coat(4, 6)
jacket_1 = Jacket(3, 4)
coat_2 = Coat(5, 7)
jacket_2 = Jacket(4, 5)
print(coat_1)
print(jacket_1)
print(coat_1.get_sq_full)
print(jacket_1.get_sq_full)
print(jacket_1.get_square_c())
print(jacket_1.get_square_j())
print(coat_2)
print(jacket_2)
print(coat_2.get_sq_full)
print(jacket_2.get_sq_full)
print(jacket_2.get_square_c())
print(jacket_2.get_square_j())

#3
class Cell:
    def __init__(self, quant):
        self.quant = int(quant)

    def __str__(self):
        return f'Результат: {self.quant * "*"}'

    def __add__(self, other):
        return Cell(self.quant + other.quant)

    def __sub__(self, other):
        if Cell(int(self.quant - other.quant)) > 0:
            return Cell(int(self.quant - other.quant))
        else:
            return f'Операция невозможна'

    def __mul__(self, other):
        return Cell(int(self.quant * other.quant))

    def __truediv__(self, other):
        return Cell(round(self.quant // other.quant))

    def make_order(self, cells):
        line = ''
        for i in range(int(self.quant / cells)):
            line += f'{"*" * cells}'
        line += f'{"*" * (self.quant % cells)}'
        return line


cell1 = Cell(33)
cell2 = Cell(22)
print(cell1)
print(cell2)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 - cell2)
print(cell1 / cell2)
print(cell2 / cell1)