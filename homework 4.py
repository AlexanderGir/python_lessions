# #Задание 1
# def sal():
#     try:
#         time = float(input('Часы '))
#         salary = int(input('Ставка '))
#         bonus = int(input('Премия '))
#         res = time * salary + bonus
#         print(f'заработная плата сотрудника: {res}')
#     except ValueError:
#         return print('ошибка')
# sal()
# 
# #Задание 2
# import itertools
#
# list_1 = [15, 2, 3, 1, 7, 5, 4, 10]
# list_2 = [el for num, el in enumerate(list_1) if list_1[num - 1] < list_1[num]]
# print(f'Исходный список: {list_1}')
# print(f'Новый список: {list_2}')
#
# #Задание 3
# print(f'Числа в пределах от 20 до 240, кратные 20 или 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')
#
# #Задание 4
# list_3 = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
# list_4 = [el for el in list_3 if list_3.count(el) == 1]
# print(f'Исходный список: {list_3}')
# print(f'Новый список: {list_4}')
#
# #Задание 5
# from functools import reduce
# def func_1(el_p, el):
#     return el_p * el
# print(f'Четные числа: {[el for el in range(99, 1001) if el % 2 == 0]}')
# print(f'Результат: {reduce(func_1, [el for el in range(99, 1001) if el % 2 == 0])}')
#
# #Задание 6
# from itertools import count
# for el in count(int(input('Введите стартовое число '))):
#     print(el)
#
# list_6 = itertools.cycle([15523, 523, 'testtest', 123.254, True])
# count = 0
# for el in list_6:
#     if count > 10:
#         break
#     print(el)
#     count +=1