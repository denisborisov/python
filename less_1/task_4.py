'''
Task 4.

Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

print("\n***** Task 4 *****")

print("\n> Let's find the biggest figure in your number.")
while True:
    user_int = input("Please, enter a big number: ")
    if user_int.isdigit() and int(user_int[0]) != 0:
        break
    else:
        print("Incorrect number. Please, try again.\n")

the_biggest_figure = int(user_int[0])
counter = 1
while counter < len(user_int):
    if the_biggest_figure < int(user_int[counter]):
        the_biggest_figure = int(user_int[counter])
    counter += 1
print(f"The biggest figure in number {user_int} is {the_biggest_figure}.")
