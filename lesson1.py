# Task 1.
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
my_int = 11
print("my_int =", my_int)

my_float = 12.0
print("my_int =", my_float)

my_str = "13"
print("my_int =", my_str)

your_first_int = int(input("Please, enter the first number: "))
your_second_int = int(input("Please, enter the second number: "))
your_name = input("By the way, what is your name? ")

your_sum = your_first_int + your_second_int
print("So, {0}, that is the sum: {1} + {2} = {3}.".format(your_name, your_first_int, your_second_int, your_sum))

# Task 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
total_seconds = int(input("Please, enter the amount of seconds: "))
hours = total_seconds // 3600
minutes = total_seconds // 60 - hours * 60
seconds = total_seconds - hours * 3600 - minutes * 60
print("{0} seconds = {1}:{2}:{3}.".format(total_seconds, hours, minutes, seconds))

# Task 3.
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_first_int = input("Please, enter a number: ")
user_second_int = user_first_int * 2
user_third_int = user_first_int * 3
sum = int(user_first_int) + int(user_second_int) + int(user_third_int)
print("{0} + {1} + {2} = {3}".format(user_first_int, user_second_int, user_third_int, sum))

# Task 4.
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_int = input("Please, enter a positive number: ")
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
revenue = float(input("Enter the income of the company: "))
expenses = float(input("Enter the expenses of the company: "))
if revenue > expenses:
    print("Income is greater than expenses. :)")
    profitability = (revenue - expenses) / revenue
    print("The profitability is {0}.".format(profitability))
    number_of_employees = int(input("Enter the number of employees: "))
    profit_per_employee = profitability / number_of_employees
    print("The profit per employee is {0}.".format(profit_per_employee))
else:
    print("Expenses are greater than income. :(")

# Task 6
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
initial_distance = int(input("Enter the initial distance you have run (km): "))
target_distance = int(input("Enter the target distance you wish to run (km): "))

current_distance = initial_distance
day_number = 1
while current_distance < target_distance:
    current_distance *= 1.1
    day_number += 1
print("On day {0} the athlete achieved a result of at least {1} km.".format(day_number, target_distance))
