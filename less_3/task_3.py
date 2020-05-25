'''
Task 3.

Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

print("\n***** Task 3 *****")
print("\n>Let's play with three numbers.")


def get_three_numbers():
    """Returns three whole numbers entered by the user.

    () -> (whole number, whole number, whole number)
    """
    while True:
        try:
            num_1, num_2, num_3, *etc = input('\nPlease, enter three whole numbers separated by the space: ').split()
            num_1, num_2, num_3 = int(num_1), int(num_2), int(num_3)
        except ValueError:
            print('Invalid numbers, please retry.')
            continue

        return num_1, num_2, num_3


def my_func(num_1, num_2, num_3):
    """Returns the max sum of two numbers among three ones.

    (number, number, number) -> (number)

    >>> my_func(-1, 2, 3)
    5
    """
    result = num_1 + num_2
    if num_1 + num_3 > result:
        result = num_1 + num_3

    if num_2 + num_3 > result:
        result = num_2 + num_3

    return result


num_1, num_2, num_3 = get_three_numbers()
max_sum = my_func(num_1, num_2, num_3)
print(f'Max sum of two numbers is {max_sum}.')
