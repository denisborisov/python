'''
Task 3.

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, веста, лето, осень).
Напишите решения через list и через dict.
'''

print("\n***** Task 3 *****")

print("\n> Let's play with months.")
while True:
    month = input("Please, enter the month in range from 1 to 12 inclusively: ")
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
        break
    else:
        print("Incorrect number. Please, try again.\n")

print("\n> Let's solve with list.")
if month in [12, 1, 2]:
    print('It is winter.')
elif month in [3, 4, 5]:
    print('It is spring.')
elif month in [6, 7, 8]:
    print('It is summer.')
else:
    print('It is autumn.')

print("\n> Let's solve with dict.")
year_dict = {
    1: "winter", 2: "winter", 3: "spring",
    4: "spring", 5: "spring", 6: "summer",
    7: "summer", 8: "summer", 9: "autumn",
    10: "autumn", 11: "autumn", 12: "winter"}
print(f'It is {year_dict[month]}')
