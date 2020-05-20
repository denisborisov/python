'''
Task 5.

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

print("\n***** Task 5 *****")

print("\n> Let's play with ratings.")

list_of_ratings = [7, 5, 3, 3, 2]
print(f"The rating list is {list_of_ratings} now.")

while True:
    rating = input("Please, enter the natural number (or q/Q if you want to stop): ")
    if rating in ['q', 'Q']:
        break
    if rating.isdigit() and int(rating) >= 0:
        rating = int(rating)
        if rating in list_of_ratings:
            position = len(list_of_ratings) - list_of_ratings[::-1].index(rating)
            list_of_ratings.insert(position, rating)
        else:
            list_of_ratings.append(rating)
            list_of_ratings.sort(reverse=True)
        print(f"The rating list is {list_of_ratings} now.")
    else:
        print("Incorrect number. Please, try again.\n")