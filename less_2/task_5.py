'''
Task 5.

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

print("\n***** Task 5 *****")

rating_list = [7, 5, 3, 3, 2]
print(f"The rating list is {rating_list} now.")

print("\n> Let's play with ratings.")
while True:
    rating = input("Please, enter the natural number (or q/Q if you want to stop): ")
    if rating in ['q', 'Q']:
        break
    if rating.isdigit() and int(rating) >= 0:
        rating = int(rating)
        if rating in rating_list:
            position = len(rating_list) - rating_list[::-1].index(rating)
            rating_list.insert(position, rating)
        else:
            rating_list.append(rating)
            rating_list.sort(reverse=True)
        print(f"The rating list is {rating_list} now.")
    else:
        print("Incorrect number. Please, try again.\n")