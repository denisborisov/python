'''
Task 3.

Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

print("\n***** Task 3 *****")
print("\n>Let's play with three numbers.")


def get_three_numbers():
    """Returns three whole numbers entered by the user."""
    while True:
        try:
            num_1, num_2, num_3, *etc = input('\nPlease, enter three whole numbers separated by the space: ').split()
            num_1, num_2, num_3 = int(num_1), int(num_2), int(num_3)
        except ValueError:
            print('Invalid numbers, please retry.')
            continue

        return num_1, num_2, num_3


def my_func(num_1: float, num_2: float, num_3: float) -> float:
    """Returns the max sum of two numbers among three ones.

    >>> my_func(-1, 2, 3)
    5
    """
    return max(num_1 + num_2, num_1 + num_3, num_2 + num_3)


num_1, num_2, num_3 = get_three_numbers()
max_sum = my_func(num_1, num_2, num_3)
print(f'Max sum of two numbers is {max_sum}.')
