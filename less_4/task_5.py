'''
Task 5.

Реализовать два небольших скрипта:

а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

print("\n***** Task 5 *****")
print("\n>Let's play with a list.")

from itertools import count, cycle

while True:
    try:
        start, stop, *argv = input("Please, enter the start and stop numbers: ").split()
        try:
            start = int(start)
            stop = int(stop)
            if stop < start:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid numbers entered, please retry.')
    except ValueError:
        print('Not enough values were provided.')


for el in count(start):
    if el > stop:
        break
    else:
        print(el, end=' ')


while True:
    try:
        list_of_values = input("\nPlease, enter the list to repeat: ").split(',')
        try:
            if list_of_values[0][0] != '[' or list_of_values[-1][-1] != ']':
                raise ValueError
            else:
                for i, elem in enumerate(list_of_values):
                    list_of_values[i] = elem.replace('[', '').replace(']', '')
                break
        except ValueError:
            print('Invalid list entered, please retry.')
    except ValueError:
        print('Not enough values were provided.')



while True:
    try:
        generation_times, *argv = input("\nPlease, enter how many times it should be repeated: ").split()
        try:
            generation_times = int(generation_times) * len(list_of_values)
            break
        except ValueError:
            print('Non a number entered, please retry.')
    except ValueError:
        print('Not enough values were provided.')


c = 0
for el in cycle(list_of_values):
    c += 1
    if c > generation_times:
        break
    else:
        print(el, end=' ')