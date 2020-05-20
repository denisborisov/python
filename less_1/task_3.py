'''
Task 3.

Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

print("\n***** Task 3 *****")

print("\n> Let's calculate the sum of three funny numbers.")
while True:
    first_number = input("Please, enter a number: ")
    if first_number.isdigit():
        break
    else:
        print("Incorrect number. Please, try again.\n")

second_number = first_number * 2
third_number = first_number * 3
sum = int(first_number) + int(second_number) + int(third_number)
print(f"{first_number} + {second_number} + {third_number} = {sum}")
