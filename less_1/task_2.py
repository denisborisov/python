'''
Task 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

print("\n***** Task 2 *****")

print("\n> Let's convert a big number of seconds into a usual format.")
while True:
    total_seconds = input("Please, enter the amount of seconds: ")
    if total_seconds.isdigit() and int(total_seconds) > 0:
        total_seconds = int(total_seconds)
        break
    else:
        print("Incorrect number. Please, try again.\n")

hours = total_seconds // 3600
minutes = total_seconds // 60 - hours * 60
seconds = total_seconds - hours * 3600 - minutes * 60
print(f"{total_seconds} seconds are equal to {hours:02}:{minutes:02}:{seconds:02} (HH:MM:SS).")
