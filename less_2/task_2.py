'''
Task 2.

Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

print("\n***** Task 2 *****")

print("\n>Let's play with a list.")

while True:
    elements_count = input("Please, enter the number of elements: ")
    if elements_count.isdigit() and int(elements_count) > 0:
        elements_count = int(elements_count)
        break
    else:
        print("Incorrect number. Please, try again.\n")

user_list = []
for i in range(elements_count):
    user_element = input("Please, enter the element of the list: ")
    user_list.append(user_element)

print(f"Your list is {user_list}.")

for i in range(elements_count):
    if i % 2 != 0:
        temp = user_list[i]
        user_list[i] = user_list[i-1]
        user_list[i-1] = temp

print(f"The altered list is {user_list}.")
