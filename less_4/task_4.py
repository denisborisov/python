'''
Task 4.

Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
'''

print("\n***** Task 4 *****")
print("\n>Let's play with a list.")

from functools import reduce

def multiply(a, b):
    return a * b

print(reduce(multiply, [n for n in range(100, 1001) if n % 2 == 0]))