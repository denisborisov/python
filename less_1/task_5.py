'''
Task 5

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

print("\n***** Task 5 *****")

print("\n> Let's calculate the profitability and the profit rate of you company.")
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
    print(f"The profitability is {profitability:.2f}.")
    number_of_employees = int(input("Enter the number of employees: "))
    profit_per_employee = profitability / number_of_employees
    print(f"The profit per employee is {profit_per_employee:.2f}.")
else:
    print("Expenses are greater than income.")
