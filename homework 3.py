#Задание 1
# def my_f(*args):
#     try:
#         ar1 = int(input("Введите первое число: "))
#         ar2 = int(input("Введите второе число: "))
#         res = ar1 / ar2
#     except ValueError:
#         return 'Ошибка'
#     except ZeroDivisionError:
#         return "Ошибка"
#     return res
# print(my_f())

#Задание 2
# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# year = int(input('Введите год рождения:'))
# city = input('Введите город проживания: ')
# email = input('Введите email:')
# phone = input('Введите телефон:')
# def m_1(name, surname, year, city, email, phone):
#     return ' '.join([name, surname, year, city, email, phone])
# print(m_1(name = 'Alex', surname = 'G', year = '1990', city = 'M', email = 'test@test.ru', phone = '89123456789'))

#Задание 3
# def fun_2(ar1, ar2, ar3):
#     if ar1 >= ar3 and ar2 >= ar3:
#         return ar1 + ar2
#     elif ar1 > ar2 and ar1 < ar3:
#         return ar1 + ar3
#     else:
#         return ar2 + ar3
# print(f'Результат: {fun_2(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')

# #Задание 4
# def fun_3(ar1, ar2):
#     return 1 / ar1 ** abs(ar2)
# print(f'Результат: {fun_3(int(input("Введите положительное число: ")), int(input("Введите целое отрицательное число: ")))}')
#
# def fun_4(ar1, ar2):
#     return ar1 ** ar2
# print(f'Результат: {fun_4(int(input("Введите положительное число: ")), int(input("Введите целое отрицательное число: ")))}')

#Задание 5
# def summ():
#     summary = 0
#     c = False
#     while c == False:
#         number = input('Введите числа, или нажмите Q для выхода: ').split()
#         a = 0
#         for el in range(len(number)):
#             if number[el] == 'q' or number[el] == 'Q':
#                 c = True
#                 break
#             else:
#                 a = a + int(number[el])
#         summary = summary + a
#         print(f'Текущая сумма: {summary}')
#     print(f'Общая сумма: {summary}')
# summ()

#Задание 6
def int_func(*args):
    w = input("Введите текст: ")
    print(w.title())
    return
int_func()