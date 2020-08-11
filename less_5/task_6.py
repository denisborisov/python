'''
Task 6.

Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

print("\n***** Task 6 *****")
print("\n>Let's play with a file.")

subjects = dict()

try:
    with open('school.txt', 'r') as file:
        for line in file:
            subject = line.split()[0][:-1]
            hours = 0
            for elem in line.split():
                if elem.split('(')[0].isdigit():
                    hours += int(elem.split('(')[0])
            subjects[subject] = hours
        print(subjects)
except FileNotFoundError:
    print("File 'school.txt' was not found.")