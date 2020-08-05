'''
Task 3.

Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].

Результат: [23, 1, 3, 10, 4, 11]
'''

import sys

print("\n***** Task 3 *****")
print("\n>Let's play with a list.")

try:
    _, *list_of_numbers = sys.argv

    try:
        for i, elem in enumerate(list_of_numbers):
            list_of_numbers[i] = int(elem.replace('[', '').replace(',', '').replace(']', ''))
        tuple_of_numbers = enumerate(list_of_numbers)
        print([elem for i, elem in tuple_of_numbers if elem not in list_of_numbers[0:i] and elem not in list_of_numbers[i+1:]])
    except ValueError:
        print('Non a number entered, please retry.')

except ValueError:
    print('Not enough values were provided.')