'''
Task 4.

Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''

print("\n***** Task 4 *****")

print("\n> Let's play with words.")

string_of_words = input("Enter a string: ")

print('The result of the processing is...')
for i, word in enumerate(string_of_words.split()):
    print(i+1, word[:10])