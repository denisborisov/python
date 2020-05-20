'''
Task 6

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

print("\n***** Task 6 *****")

print("\n> Let's calculate the number of days needed to get you towards your goal.")
while True:
    while True:
        initial_distance = input("Enter the initial distance you have run (km): ")
        if initial_distance.isdigit():
            initial_distance = int(initial_distance)
            break
        else:
            print("Incorrect number. Please, try again.\n")

    while True:
        target_distance = input("Enter the target distance you wish to run (km): ")
        if target_distance.isdigit():
            target_distance = int(target_distance)
            break
        else:
            print("Incorrect number. Please, try again.\n")

    if initial_distance < target_distance:
        break
    else:
        print("The initial distance must be lower than the target distance. Please, try again.\n")

current_distance = initial_distance
day_number = 1
while current_distance < target_distance:
    current_distance *= 1.1
    day_number += 1
print(f"On day {day_number} the athlete achieved a result of at least {target_distance} km.")
