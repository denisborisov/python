'''
Task 1.

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

print("\n***** Task 1 *****")
print("\n>Let's play with division.")


def get_two_numbers():
    """Returns two whole numbers entered by the user.

    () -> (whole number, whole number)
    """
    while True:
        try:
            num_1, num_2, *etc = input('\nPlease, enter two whole numbers separated by the space: ').split()
            num_1, num_2 = int(num_1), int(num_2)
        except ValueError:
            print('Invalid numbers, please retry.')
            continue

        return num_1, num_2


def division(dividend: float, divisor: float) -> float:
    """Returns the result of division of two numbers.
    Returns 0 in case of divisor = 0.

    >>> division(4, 2)
    2.0
    """
    return 0 if divisor == 0 else dividend / divisor


dividend, divisor = get_two_numbers()
quotient = division(dividend, divisor)
print(f'The result of division is {quotient}.')
