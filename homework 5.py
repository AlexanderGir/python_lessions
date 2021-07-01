# #1
# f_1 = open('hm_file_1.txt', 'w')
# line = input('Введите текст:\n')
# while line:
#     f_1.writelines(line)
#     line = input('Введите текст, для завершения оставьте поле пустым и нажмите Enter:\n')
#     if not line:
#         break
# f_1.close()

# #2
# f_2 = open('hm_file_2.txt', 'r')
# text = f_2.readlines()
# print(f'Количество строк: {len(text)}')
# f_2.close()
# f_2 = open('hm_file_2.txt', 'r')
# text = f_2.readlines()
# for i in range(len(text)):
#     print(f'{i + 1} символ/ов/а в строке {len(text[i])}')
# f_2 = open('hm_file_2.txt', 'r')
# text = f_2.read()
# text = text.split()
# print(f'Общее количество слов - {len(text)}')
# f_2.close()

# #3
# with open('hm_file_3.txt', 'r', encoding='utf-8') as f_3:
#     salary = []
#     x = []
#     f_3 = f_3.read().split('\n')
#     for i in f_3:
#         i = i.split()
#         if int(i[1]) < 20000:
#             x.append(i[0])
#         salary.append(i[1])
# print(f'Оклад меньше 20.000 - {x}, средний оклад {sum(map(int, salary)) / len(salary)}')

# #4
# change = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# f_4 = []
# with open('hm_file_4.txt', 'r') as f_5:
#     for i in f_5:
#         i = i.split(' ', 1)
#         f_4.append(change[i[0]] + '  ' + i[1])
#     print(f_4)
#
# with open('hm_file_5.txt', 'x') as f_6:
#     f_6.writelines(f_4)

# #5
#
# with open('hm_file_6.txt', 'w+') as f_7:
#     try:
#         line = input('Введите цифры: \n')
#         f_7.writelines(line)
#         num = line.split()
#         print(sum(map(int, num)))
#     except IOError:
#         print('Ошибка')
#     except ValueError:
#         print('Ошибка ввода-вывода')

# #6
# with open('hm_file_7.txt', 'r') as f_8:
#     for line in f_8:
#         subject, lecture, practice, lab = line.split()
#         sub[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Сумма часов: \n {sub}')

#7
# import json
# profit = {}
# profit_1 = 0
# prof_aver = 0
# i = 0
# with open('hm_file_8.txt', 'r') as file:
#     for line in file:
#         name, firm, earning, charge = line.split()
#         profit[name] = int(earning) - int(charge)
#         if profit[name] >= 0:
#             profit_1 = profit_1 + profit[name]
#             i += 1
#     if i != 0:
#         prof_aver = profit_1 / i
#         print(f'Средняя прибыль - {prof_aver}')
#     else:
#         print(f'Работа в убыток')
#     print(f'Прибыль компаний - {profit}')
#
# with open('hm_file_8.json', 'w') as w_j:
#     json.dump(profit, w_j)