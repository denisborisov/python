'''
Task 4.

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

print("\n***** Task 4 *****")
print("\n>Let's play with powering.")


def get_two_numbers():
    """Returns two whole numbers entered by the user.

    () -> (positive float number, negative whole number)
    """
    while True:
        try:
            x = float(input('\nPlease, enter the first float number (positive): '))
        except ValueError:
            print('Invalid number, please retry.')
            continue

        if x <= 0:
            print('Invalid number, please retry.')
            continue

        break

    while True:
        try:
            y = int(input('\nPlease, enter the second whole number (negative): '))
        except ValueError:
            print('Invalid number, please retry.')
            continue

        if y >= 0:
            print('Invalid number, please retry.')
            continue

        break

    return x, y


def my_func_1(x: float, y: int) -> float:
    """Returns the result of pow(x, y).

    >>> my_func_1(2.0, -2)
    0.25
    """
    return x**y

def my_func_2(x: float, y: int) -> float:
    """Returns the result of pow(x, y).

    >>> my_func_2(2, -2)
    0.25
    """
    result = 1
    for i in range(abs(y)):
        result /= x
    return result


x, y = get_two_numbers()

# The first method
result_1 = my_func_1(x, y)
print(f'1st method: the result of {x}^({y}) is {result_1}')

# The second method
result_2 = my_func_2(x, y)
print(f'2nd method: the result of {x}^({y}) is {result_2}')