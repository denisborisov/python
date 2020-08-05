'''
Task 1.

Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys

print("\n***** Task 1 *****")
print("\n>Let's play with salary.")

def calculate_salary(hours, rate, bonus):
    return hours * rate + bonus

try:
    _, hours, rate, bonus, *etc = sys.argv
    try:
        hours, rate, bonus = int(hours), int(rate), int(bonus)
        print('Salary is', calculate_salary(hours, rate, bonus))
    except ValueError:
        print('Non a number entered, please retry.')

except ValueError:
    print('Not enough values were provided.')