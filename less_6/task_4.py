'''
Task 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

print("\n***** Task 4 *****")
print("\n>Let's play with a class.")


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.name} began to go.')

    def stop(self):
        print(f'The {self.name} stopped.')

    def turn(self, direction):
        print(f'The {self.name} turned {direction}.')

    def show_speed(self):
        print(f'The speed of the {self.name} is {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Caution! {self.name}'s speed ({self.speed}) is too high!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Caution! Your car speed ({self.speed}) is too high!')


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'beige', 'Toyota', False)
town_car.go()
town_car.show_speed()
print()

sport_car = SportCar(100, 'red', 'Jaguar', False)
sport_car.show_speed()
sport_car.stop()
print()

work_car = WorkCar(50, 'black', 'Aurus', False)
work_car.turn('left')
work_car.show_speed()
print()

police_car = PoliceCar(50, 'white', 'Volvo', True)
police_car.show_speed()
print()