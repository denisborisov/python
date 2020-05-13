# Task 1.
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
print("\n***** Task 1 *****")

my_int = 11
print("my_int =", my_int)

my_float = 12.0
print("my_float =", my_float)

my_str = "13"
print("my_str =", my_str)

while True:
    first_number = input("Please, enter the first number: ")
    if first_number.isdigit():
        first_number = int(first_number)
        break
    else:
        print("Incorrect number. Please, try again.\n")

while True:
    second_number = input("Please, enter the second number: ")
    if second_number.isdigit():
        second_number = int(second_number)
        break
    else:
        print("Incorrect number. Please, try again.\n")

user_name = input("By the way, what is your name? ")

sum = first_number + second_number
print("So, {0}, that is the sum: {1} + {2} = {3}.".format(user_name, first_number, second_number, sum))

# Task 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
print("\n***** Task 2 *****")

while True:
    total_seconds = input("Please, enter the amount of seconds: ")
    if total_seconds.isdigit() and int(total_seconds) > 0:
        total_seconds = int(total_seconds)
        break
    else:
        print("Incorrect number. Please, try again.\n")

hours = total_seconds // 3600
minutes = total_seconds // 60 - hours * 60
seconds = total_seconds - hours * 3600 - minutes * 60
print("{0} seconds = {1}:{2}:{3}.".format(total_seconds, hours, minutes, seconds))

# Task 3.
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("\n***** Task 3 *****")

while True:
    first_number = input("Please, enter a number: ")
    if first_number.isdigit():
        break
    else:
        print("Incorrect number. Please, try again.\n")

second_number = first_number * 2
third_number = first_number * 3
sum = int(first_number) + int(second_number) + int(third_number)
print("{0} + {1} + {2} = {3}".format(first_number, second_number, third_number, sum))

# Task 4.
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
print("\n***** Task 4 *****")

while True:
    user_int = input("Please, enter a number: ")
    if user_int.isdigit() and int(user_int) > 0:
        break
    else:
        print("Incorrect number. Please, try again.\n")

the_biggest_figure = int(user_int[0])
counter = 1
while counter < len(user_int):
    if the_biggest_figure < int(user_int[counter]):
        the_biggest_figure = int(user_int[counter])
    counter += 1
print("The biggest figure in number {0} is {1}.".format(user_int, the_biggest_figure))

# Task 5
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print("\n***** Task 5 *****")

while True:
    revenue = input("Enter the income of the company: ")
    if revenue.isdigit():
        revenue = int(revenue)
        break
    else:
        print("Incorrect number. Please, try again.\n")

while True:
    expenses = input("Enter the expenses of the company: ")
    if expenses.isdigit():
        expenses = int(expenses)
        break
    else:
        print("Incorrect number. Please, try again.\n")

if revenue > expenses:
    print("Income is greater than expenses.")
    profitability = (revenue - expenses) / revenue
    print("The profitability is {0}.".format(profitability))
    number_of_employees = int(input("Enter the number of employees: "))
    profit_per_employee = profitability / number_of_employees
    print("The profit per employee is {0}.".format(profit_per_employee))
else:
    print("Expenses are greater than income.")

# Task 6
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
print("\n***** Task 6 *****")

while True:
    while True:
        initial_distance = input("Enter the initial distance you have run (km): ")
        if initial_distance.isdigit():
            initial_distance = int(initial_distance)
            break
        else:
            print("Incorrect number. Please, try again.\n")

    while True:
        target_distance = input("Enter the target distance you wish to run (km): ")
        if target_distance.isdigit():
            target_distance = int(target_distance)
            break
        else:
            print("Incorrect number. Please, try again.\n")

    if initial_distance < target_distance:
        break
    else:
        print("The initial distance must be lower than the target distance. Please, try again.\n")

current_distance = initial_distance
day_number = 1
while current_distance < target_distance:
    current_distance *= 1.1
    day_number += 1
print("On day {0} the athlete achieved a result of at least {1} km.".format(day_number, target_distance))
