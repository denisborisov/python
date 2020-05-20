'''
Task 4.

Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''

print("\n***** Task 4 *****")

print("\n> Let's play with words.")

user_string = input("Enter a string: ")

print('The result of the processing is...')
for i, word in enumerate(user_string.split()):
    print(i+1, word[:10])