'''
Task 1.

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

print("\n***** Task 1 *****")
print("\n>Let's play with date.")


class Date:
    date = {}

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def get_date_from(cls, date: str) -> dict:
        first_hyphen_pos = date.find('-')
        second_hyphen_pos = first_hyphen_pos + date[first_hyphen_pos+1:].find('-') + 1

        day = int(date[:first_hyphen_pos])
        month = int(date[first_hyphen_pos+1:second_hyphen_pos])
        year = int(date[second_hyphen_pos+1:])

        if cls.validate(cls, day, month, year):
            cls.date = {'day': day, 'month': month, 'year': year}

        return cls.date

    @staticmethod
    def validate(cls, day, month, year) -> bool:
        if day in range(1, 31) and month in range(1, 12) and year in range(1, 9999):
            return True
        else:
            return False


my_date = Date('21-08-1990')
print(Date.get_date_from('21-08-1990'))