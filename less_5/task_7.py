'''
Task 7.

Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''

print("\n***** Task 7 *****")
print("\n>Let's play with a file.")

import json

try:
    with open('firms.txt', 'r') as file:
        firms = dict()
        count = 0
        total_profit = 0
        for line in file:
            line = line.split()
            firm = line[0]
            if line[3].isdigit() and line[2].isdigit():
                profit = int(line[3]) - int(line[2])
                if profit > 0:
                    total_profit += profit
                    count += 1
                firms[firm] = profit
        if count > 0:
            average_profit = total_profit / count
        else:
            average_profit = 0
        profit_list = [firms]
        profit_list.append({"average_profit": average_profit})
except FileNotFoundError:
    print("File 'firms.txt' was not found.")

with open('firms.json', 'w') as file:
    json.dump(profit_list, file)