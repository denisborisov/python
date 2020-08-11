'''
Task 1.

Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

print("\n***** Task 1 *****")
print("\n>Let's play with a file.")

user_string = input('Введите построчно данные для записи в файл. Окончанием ввода является пустая строка.\n> ')

with open('user_file.txt', 'w') as file:
    while user_string:
        file.write(user_string + '\n')
        user_string = input('> ')