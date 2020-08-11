'''
Task 5.

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

print("\n***** Task 5 *****")
print("\n>Let's play with a file.")

with open('fibo.txt', 'w') as file:
    file.write('1 1 2 3 5 8 13 21 34 55 89 144')

with open('fibo.txt', 'r') as file:
    content = file.read().split()
    sum = 0
    for num in content:
        if num.isdigit():
            sum += int(num)
    print(f'Sum = {sum}')