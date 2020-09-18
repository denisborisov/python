'''
Task 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.

При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''

print("\n***** Task 2 *****")
print("\n>Let's play with exceptions.")


class ZeroDivisionException (Exception):
    def __init__(self, text):
        self.text = text


while True:
    dividend = input("\nEnter a dividend: ")
    if dividend.isdigit():
        dividend = int(dividend)
        break
    else:
        print(f'{dividend} is not a number. Try again.')

while True:
    divisor = input("\nEnter a divisor: ")
    try:
        if divisor.isdigit():
            divisor = int(divisor)
            if divisor == 0:
                raise ZeroDivisionException('The divisor cannot be equal zero! Try again.')
            break
        else:
            print(f'{divisor} is not a number. Try again.')
    except ZeroDivisionException as zde:
        print(zde)

print(f'Quotient is {dividend / divisor}.')