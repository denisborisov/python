'''
Task 6.

Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

print("\n***** Task 6 *****")
print("\n>Let's play with a list.")

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

while True:
    try:
        number, *argv = input("Please, enter a positive number: ").split()
        try:
            number = int(number)
            if number <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid number entered, please retry.')
    except ValueError:
        print('Not enough values were provided.')

i = 0
for el in fact(number):
    i += 1
    print(f'{i}! = ', el)