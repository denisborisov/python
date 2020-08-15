'''
Task 5.

Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

print("\n***** Task 5 *****")
print("\n>Let's play with a class.")


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.\n')


class Pen(Stationery):
    def draw(self):
        print(f'Нарисовано by {self.title}.\n')


class Pencil(Stationery):
    def draw(self):
        print(f'Нарисовано by {self.title}.\n')


class Handle(Stationery):
    def draw(self):
        print(f'Нарисовано by {self.title}.\n')


stationery = Stationery('канцелярия')
stationery.draw()

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()