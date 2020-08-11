'''
Task 4.

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

print("\n***** Task 4 *****")
print("\n>Let's play with a file.")

try:
    with open('eng_numbers.txt', 'r') as in_file, open('rus_numbers.txt', 'w') as out_file:
        for line in in_file:
            line = line.replace('One', 'Один')
            line = line.replace('Two', 'Два')
            line = line.replace('Three', 'Три')
            line = line.replace('Four', 'Четыре')
            out_file.write(line)
except FileNotFoundError:
    print("File 'eng_numbers.txt' was not found.")