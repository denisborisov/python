'''
Task 1.

Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

print("\n***** Task 1 *****")

my_list = [0, 3.1415926, "Denis Borisov", ("my", "tuple"), [1, 2, 3, 4, 5], {"a", "set"}, {"a" : "dictionary"}]

for element in my_list:
    if type(element) == dict:
        print(f"{element} -- a dictionary, of course")
    else:
        print(element)