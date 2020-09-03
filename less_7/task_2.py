'''
Task 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

print("\n***** Task 2 *****")
print("\n>Let's play with clothes.")


class Clothes(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def fabric_consumption(self) -> float:
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def fabric_consumption(self):
        return self.size/6.5 + 0.5

    @property
    def size(self):
        return self.__size


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    def fabric_consumption(self):
        return 2 * self.height + 0.3

    @property
    def height(self):
        return self.__height


suit = Suit('D&G', 20)
coat = Coat('Henderson', 8)

clothes = [suit, coat]

fabric_consumption = 0
for c in clothes:
    fabric_consumption += c.fabric_consumption()

print(f'Fabric consumption is {format(fabric_consumption, ".2f")}.')