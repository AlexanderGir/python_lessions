#1
# from time import sleep
#
#
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         a = 0
#         while a < 3:
#             print(f'Сигнал светофора: {TrafficLight.__color[a]}')
#             if a == 0:
#                 sleep(7)
#             elif a == 1:
#                 sleep(5)
#             elif a == 2:
#                 sleep(10)
#             a += 1
#
#
# TrafficLight = TrafficLight()
# TrafficLight.running()

# #2
# class Road:

#     def __init__(self, _length, _width, _mass1, _thickness):
#         self._length = _length
#         self._width = _width
#         self._mas = _mass1
#         self._thickness = _thickness
#
#     def mass(self):
#         return self._length * self._width * self._mas * self._thickness
#
#
# r = Road(10, 7000, 20, 0.1)
# print(r.mass())

#3
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
#
# p = Position('Alex', 'Bishop', 'Hunter', 7777, 666)
# print(p.get_full_name())
# print(p.position)
# print(p.get_total_income())

#4
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'{self.name} начала движение'
#
#     def stop(self):
#         return f'{self.name} остановилась'
#
#     def turn_right(self):
#         return f'{self.name} повернула направо'
#
#     def turn_left(self):
#         return f'{self.name} повернула налево'
#
#     def show_speed(self):
#         return f'Скорость {self.name} составляет: {self.speed}'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed1(self):
#         print(f'Скорость {self.name} составляет: {self.speed}')
#
#         if self.speed > 40:
#             return f'Скорость {self.name} превышена'
#         else:
#             return f'Скорость {self.name} нормальная'
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed2(self):
#         print(f'Скорость {self.name} составляет: {self.speed}')
#
#         if self.speed > 60:
#             return f'Скорость {self.name} превышена'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} - копы'
#         else:
#             return f'{self.name} - не копы'
#
#
# bmw = SportCar(200, 'Red', 'BMW', False)
# audi = TownCar(35, 'White', 'Audi', False)
# gazel = WorkCar(70, 'Blue', 'Gazel', False)
# volvo = PoliceCar(110, 'Black', 'Volvo', True)
# print(volvo.turn_left())
# print(f'{gazel.go()}. {gazel.show_speed()} км/ч')
# print(audi.show_speed1())
# print(gazel.show_speed2())
# print(volvo.show_speed())

#5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Используется {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Используется {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Используется {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())