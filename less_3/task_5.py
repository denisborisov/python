'''
Task 5.

Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

print("\n***** Task 5 *****")
print("\n>Let's play with sum.")


def my_sum(list_of_nums: list) -> float:
    """Returns the sum of numbers from list_of_nums.
    Stop if non-number is trying to be processed.

    >>> my_sum([2.0, -5, 'q', 3.14])
    -3.0
    """
    result = 0.0
    try:
        for num in list_of_nums:
            result += float(num)
    finally:
        return result


total = 0.0
while True:
    user_input = input('\nPlease, enter numbers separated by the space (enter non-number / non-blank to stop): ').split()
    try:
        total += sum(map(float, user_input))
    except ValueError:
        total += my_sum(user_input)
        break
    finally:
        print(f'Current sum: {total}.')
