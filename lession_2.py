#Задание 1
li = [24, 'text', 26.45, True]
for i in range(len(li)):
    print(type(li[i]))

#Задание 2
elements = int(input("Enter: "))
list_1 = []
i = 0
elem = 0
while i < elements:
    list_1.append(input("Enter: "))
    i += 1
for el in range(int(len(list_1) / 2)):
    list_1[elem], list_1[elem + 1] = list_1[elem + 1], list_1[elem]
    elem += 2
print(list_1)

#Задание 3
s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите месяц: "))
if month == 12 or month == 1 or month == 2:
    print(s_dict.get(1))
    print(s_list[0])
elif month == 3 or month == 4 or month == 5:
    print(s_dict.get(2))
    print(s_list[1])
elif month == 6 or month == 7 or month == 8:
    print(s_dict.get(3))
    print(s_list[2])
elif month == 9 or month == 10 or month == 11:
    print(s_dict.get(4))
    print(s_list[3])
else:
    print("Ошибка")

#Задание 4
a = input("Введите текст: ")
b = []
num = 1
for el in range(a.count(' ') + 1):
    b = a.split()
    if len(str(b)) <= 10:
        print(f" {num} {b[el]}")
        num += 1
    else:
        print(f" {num} {b[el][0:10]}")
        num += 1

#Задание 5
list_2 = [8, 4, 3, 3, 2]
num = int(input("Введите число (для выхода введите 666): "))
while num != 666:
    for el in range(len(list_2)):
        if list_2[el] == num:
            list_2.insert(el + 1, num)
            break
        elif list_2[0] < num:
            list_2.insert(0, num)
        elif list_2[-1] > num:
            list_2.append(num)
        elif list_2[el] > num and list_2[el + 1] < num:
            list_2.insert(el + 1, num)
    print(list_2)
    num = int(input("Введите число "))
