'''
Task 6.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''

print("\n***** Task 6 *****")
print("\n>Let's play with warehouse.")


class Department:

    def __init__(self, name):
        self.name = name

    def get_office_equipment(self, warehouse,  item: str, count: int = 1):
        warehouse.give_to_department(self.name, item, count)

    def return_office_equipment(self, warehouse,  item: str, count: int = 1):
        warehouse.return_from_department(self.name, item, count)


class Warehouse:
    office_equipment = {
        'item':
            {
                'department': 'count'
            }
    }

    def __init__(self):
        self.office_equipment = {}

    def lay_in(self, *argv):
        for el in argv:
            item = type(el).__name__.lower()
            if item not in self.office_equipment:
                self.office_equipment[item] = {'in stock': 1}
            else:
                self.office_equipment[item]['in stock'] += 1

    def give_to_department(self, department_name, item: str, count: int):
        if item not in self.office_equipment:
            print(f'You required {item}(s/es). There is no such office equipment at all.')
        elif self.office_equipment[item]['in stock'] == 0:
            print(f'All {item}(s/es) has been already given out to the other departments.')
        elif self.office_equipment[item]['in stock'] < count:
            print(f'We have only {self.office_equipment[item]["in stock"]} {item}(s/es). Not {count}.')
        elif department_name not in self.office_equipment[item]:
            self.office_equipment[item][department_name] = count
            self.office_equipment[item]['in stock'] -= count
        else:
            self.office_equipment[item][department_name] += count
            self.office_equipment[item]['in stock'] -= count

    def return_from_department(self, department_name, item: str, count: int):
        if item not in self.office_equipment:
            print(f'We never had {item}(s/es) before.')
        elif department_name not in self.office_equipment[item]:
            print(f'We never gave this {item}(s/es) to the {department_name} department.')
        elif self.office_equipment[item][department_name] == 0:
            print(f'Our records are saying that you haven\'t got this {item}(s/es).')
        elif self.office_equipment[item][department_name] < count:
            print(f'Our records are saying that you haven\'t got so many ({count}) {item}(s/es).')
        else:
            self.office_equipment[item][department_name] -= count
            self.office_equipment[item]['in stock'] += count


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


p1 = Printer(100, 10, 20, 30)
p2 = Printer(100, 10, 20, 30)
s1 = Scanner(600, 10, 20, 30)
s2 = Scanner(600, 10, 20, 30)
x1 = Xerox(False, 10, 20, 30)
x2 = Xerox(True, 10, 20, 30)

w = Warehouse()
w.lay_in(p1, p2)
w.lay_in(s1, s2)
w.lay_in(x1, x2)
print('\n>> The initial office equipment situation in the warehouse.')
print(w.office_equipment)

d1 = Department('Sales')
d2 = Department('Marketing')
d3 = Department('Developing')

d1.get_office_equipment(w, 'printer')
d1.get_office_equipment(w, 'scanner')
print('\n>> We gave some equipment to the first department.')
print(w.office_equipment)

d2.get_office_equipment(w, 'printer')
d2.get_office_equipment(w, 'scanner')
d2.get_office_equipment(w, 'xerox')
print('\n>> We gave some equipment to the second department.')
print(w.office_equipment)

print('\n>> Try to get some items from the warehouse.')
d1.get_office_equipment(w, 'computer')
d1.get_office_equipment(w, 'printer')
d1.get_office_equipment(w, 'xerox', 2)

print('\n>> Try to return some items to the warehouse.')
d1.return_office_equipment(w, 'computer')
d3.return_office_equipment(w, 'printer')
d1.return_office_equipment(w, 'printer', 2)
d1.return_office_equipment(w, 'printer')
d1.return_office_equipment(w, 'printer')