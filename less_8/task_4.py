'''
Task 4.

Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

print("\n***** Task 4 *****")
print("\n>Let's play with warehouse.")


class Warehouse:
    def __init__(self):
        self.office_equipment = []

    def add(self, *argv):
        for el in argv:
            self.office_equipment.append(el)


class OfficeEquipment:
    def __init__(self, height: int, length: int, width: int):
        self.height = height
        self.length = length
        self.width = width


class Printer(OfficeEquipment):
    def __init__(self, speed: int, *argv):
        super().__init__(*argv)
        self.speed = speed

    def __repr__(self):
        return f'A printer with speed {self.speed}'


class Scanner(OfficeEquipment):
    def __init__(self, resolution: int, *argv):
        super().__init__(*argv)
        self.resolution = resolution

    def __repr__(self):
        return f'A scanner with resolution {self.resolution}'


class Xerox(OfficeEquipment):
    def __init__(self, is_fax_enabled: bool, *argv):
        super().__init__(*argv)
        self.is_fax_enabled = is_fax_enabled

    def __repr__(self):
        return f'A xerox {"with" if self.is_fax_enabled else "without"} fax'


p = Printer(100, 10, 20, 30)
s = Scanner(600, 10, 20, 30)
x = Xerox(False, 10, 20, 30)

w = Warehouse()
w.add(p, s, x)
print(w.office_equipment)
