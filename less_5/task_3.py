'''
Task 3.

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

print("\n***** Task 3 *****")
print("\n>Let's play with a file.")

try:
    with open('employees.txt', 'r') as file:
        count = 0
        total_salary = 0
        for line in file:
            if line.isdigit():
                salary = int(line)
                total_salary += salary
                if salary < 20000:
                    print(f'{surname} has salary less than 20.000.')
            else:
                surname = line[:-1]
                count += 1
        if count > 0:
            print(f'The average salary is {total_salary/count}')
except FileNotFoundError:
    print("File 'employees.txt' was not found.")