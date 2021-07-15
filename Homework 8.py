# #1
# class Data:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def ext(cls, day_month_year):
#         date = []
#
#         for i in day_month_year.split():
#             if i != '-': date.append(i)
#
#         return int(date[0]), int(date[1]), int(date[2])
#
#     @staticmethod
#     def check(day, month, year):
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2021 >= year >= 0:
#                     return f'Данные приняты'
#                 else:
#                     return f'Введен неверный год'
#             else:
#                 return f'Введен неверный месяц'
#         else:
#             return f'Введен неверный день'
#
#     def __str__(self):
#         return f'Дата: {Data.ext(self.day_month_year)}'
#
#
# t = Data('15 - 07 - 2021')
# print(t)
# print(Data.check(9, 4, 2023))
# print(t.check(5, 22, 2021))
# print(Data.check(15, 7, 2021))

# # №2
# class Null:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def div(a, b):
#         try:
#             return a / b
#         except:
#             return (f"Делить на ноль нельзя")
#
#
# div = Null(124, 100)
# print(Null.div(177, 0))
# print(Null.div(10000, 2))

# 3
# class Err:
#
#     def __init__(self, *data):
#         self.data = []
#
#     def input(self):
#         while True:
#             try:
#                 check = int(input('Введите числа (для выхода нажмите Z): '))
#                 self.data.append(check)
#                 if check == 'Z' or check == 'z':
#                     return f'Итоговый список: {self.data} \n '
#                 else:
#                     print(f'Последняя версия списка: {self.data} \n ')
#             except:
#                 cancel = input(f'Для продолжения нажмите N, для выхода нажмите любую другую клавишу: ')
#                 if cancel == 'N' or cancel == 'n':
#                     print(exc.input())
#                 else:
#                     return f'Итоговый список: {self.data} \n'
#
#
# exc = Err(1)
# print(exc.input())

#4
class Store:

    def __init__(self, name, price, quantity, *data):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all_store = []
        self.store = []
        self.unit_1 = {'Модель: ': self.name, 'Цена: ': self.price, 'Количество: ': self.quantity}

    def __str__(self):
        return f'{self.name} по цене {self.price} в количестве {self.quantity} шт.'

    def data(self):
        q = input(f'Для продолжения нажмите - N, для выхода - любую другую  клавишу')
        if q == 'N' or q == 'n':
            try:
                unit_2 = input(f'Введите название: ')
                price_1 = int(input(f'Введите цену: '))
                quantity_1 = int(input(f'Введите количество: '))
                total = {'Модель': unit_2, 'Цена': price_1, 'Количество': quantity_1}
                self.unit_1.update(total)
                self.store.append(self.unit_1)
                print(f'Текущий список оргтехники -\n {self.store}')
                return Store.data(self)
            except:
                return f'Ошибка ввода данных'
        else:
            self.all_store.append(self.store)
            print(f'Весь склад -\n {self.all_store}')
            return f'Выход'


class Printer(Store):
    def print(self, numb):
        self.numb = numb
        return f'Доставка {self.numb} принтеров'


class Scanner(Store):
    def scan(self, numb):
        self.numb = numb
        return f'Доставка {self.numb} сканеров'


class Copier(Store):
    def cop(self, numb):
        self.numb = numb
        return f'Доставка {self.numb} копиров'


unit_1 = Printer('ABC', 1678, 3, 122)
unit_2 = Scanner('CCC', 19888, 8, 17)
unit_3 = Copier('XDF', 1298, 4, 79)
print(unit_1.data())
print(unit_2.data())
print(unit_3.data())

#7
class ComNum:
    def __init__(self, a, b, *data):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма: ')
        return f'с = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение: ')
        return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


x_1 = ComNum(6, -7)
x_2 = ComNum(2, 9)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)