#a = 20
#b = 17
#print(a, b)

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#print(name, age)

# time = int(input("Enter time in sec: "))
# h = time // 3600
# m = time % 3600 // 60
# s = time % 3600 % 60
# print(f"time: {h}:{m}:{s}")

# ax = int(input("Enter your number: "))
# sum = ax + int(str(ax) + str(ax)) + int(str(ax) + str(ax) + str (ax))
# print("Summary: ", sum)

# num = int(input("Enter your number: "))
# i = num % 10
# num = num // 10
# while num >= 1:
#     if num % 10 > i:
#         i = num % 10
#     num = num // 10
# print("Наибольшая цифра в числе ", i)

# gain = float(input("Enter gain: "))
# costs = float(input("Enter costs: "))
# profit = (gain - costs) / gain
# if gain > costs:
#     print("Working with profit: ", profit)
#     employees = int(input("Enter number of employees: "))
#     print("Profit for person: ", profit / employees)
# elif gain == costs:
#     print("Working at zero")
# else:
#     print("Working at a loss")

a = int(input("Значение a = "))
b = int(input("Значение b = "))
day = 1
# print(f"День {day}: {a} км")
while a < b:
    a = a + (a / 10)
    day += 1
    # print(f"День {day}: {a} км")
print("День достижения спортсменом результата - ", day)