'''
Task 2.

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

print("\n***** Task 2 *****")
print("\n>Let's play with a file.")

try:
    with open('song.txt', 'r') as file:
        lines = file.readlines()
        print(f'Количество строк: {len(lines)}')
        for number, line in enumerate(lines):
            print(f'{number+1}-я строка состоит из {len(line.split())} слов.')
except FileNotFoundError:
    print("File 'song.txt' was not found.")