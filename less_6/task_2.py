'''
Task 2.

Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

print("\n***** Task 2 *****")
print("\n>Let's play with a class.")

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_road_mass(self, mass_quote_kg, thickness_cm):
        return self._length * self._width * mass_quote_kg * thickness_cm / 100 / 1000

my_road = Road(5000, 20)

print(f'The total mass of the road will be {my_road.calculate_road_mass(25, 5)} tons.')