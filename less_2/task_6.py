'''
Task 6.

Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
'''

print("\n***** Task 6 *****")

print("\n> Let's play with goods.")
print("Please, enter the info about the articles of trade.")

list_of_goods = []
counter = 0
while True:
    name = input("\nName of item: ")

    while True:
        price = input("Price: ")
        if price.isdigit() and int(price) >= 0:
            price = int(price)
            break
        else:
            print("Incorrect number. Please, try again.\n")

    while True:
        quantity = input("Quantity: ")
        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            break
        else:
            print("Incorrect number. Please, try again.\n")

    unit = input("Measurement unit: ")

    counter += 1

    list_of_goods.append((counter, {"name" : name, "price" : price, "quantity" : quantity, "unit" : unit}))

    while True:
        proceed = input('Do you want to proceed (Y/N): ')
        if proceed in ['Y', 'N', 'y', 'n']:
            break
        else:
            print('Invalid character. Please, try again.')

    if proceed in ['N', 'n']:
        break

print('\nThe list of your goods:')
print('[')
for item in list_of_goods:
    print(item)
print(']')

print("\n> Let's provide the data alanytics.")

goods_summary = {"name" : [], "price" : [], "quantity" : [], "unit" : []}
for item in list_of_goods:
    for key, value in item[1].items():
        goods_summary[key].append(value)

print('\nThe summary of your goods:')
print('{')
for key, value in goods_summary.items():
    print(f"{key}: {value}")
print('}')