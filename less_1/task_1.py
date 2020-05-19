'''
Task 1.

Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

print("\n***** Task 1 *****")

print("\n> Let me play with some variables.")
my_int = 11
print("my_int =", my_int)

my_float = 12.0
print("my_float =", my_float)

my_str = "13"
print("my_str =", my_str)

print("\n> Let's calculate the sum of two numbers.")
while True:
    first_number = input("Please, enter the first number: ")
    if first_number.isdigit():
        first_number = int(first_number)
        break
    else:
        print("Incorrect number. Please, try again.\n")

while True:
    second_number = input("Please, enter the second number: ")
    if second_number.isdigit():
        second_number = int(second_number)
        break
    else:
        print("Incorrect number. Please, try again.\n")

user_name = input("By the way, what is your name? ")

sum = first_number + second_number
print(f"So, {user_name}, that is the sum: {first_number} + {second_number} = {sum}.")
