'''
Task 2.

Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].

Результат: [12, 44, 4, 10, 78, 123].

Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

Подсказка: использовать функцию range() и генератор.
'''

import sys

print("\n***** Task 2 *****")
print("\n>Let's play with a list.")

def next_greater_element(list_of_numbers):
    for i, elem in enumerate(list_of_numbers):
        if i > 0 and elem > list_of_numbers[i-1]:
            yield elem

print("\n***** Subask 2.1 *****")
try:
    _, *list_of_numbers = sys.argv

    try:
        for i, elem in enumerate(list_of_numbers):
            list_of_numbers[i] = int(elem.replace('[', '').replace(',', '').replace(']', ''))
        print([elem for elem in next_greater_element(list_of_numbers)])
    except ValueError:
        print('Non a number entered, please retry.')

except ValueError:
    print('Not enough values were provided.')

print("\n***** Subask 2.2 *****")
print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])