'''
Task 2.

Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

print("\n***** Task 2 *****")
print("\n>Let's play with user data.")

user_data_template = {'first_name': '',
                      'last_name': '',
                      'birth_year': 0,
                      'city': '',
                      'email': '',
                      'phone': '',
                      }


def get_user_birth_year() -> int:
    """Returns a year of birth entered by the user."""
    while True:
        try:
            birth_year = int(input('Please, enter your year of birth: '))
        except ValueError:
            print('Invalid year, please retry.\n')
            continue

        if not (1900 <= birth_year <= 2020):
            print('Invalid year, please retry.\n')
            continue

        return birth_year


def get_user_data() -> dict:
    """Returns a dictionary of user data."""
    user_data = {}
    user_data['first_name'] = input('Enter your first name: ')
    user_data['last_name'] = input('Enter your last name: ')
    user_data['birth_year'] = get_user_birth_year()
    user_data['city'] = input('Enter your city: ')
    user_data['email'] = input('Enter your email: ')
    user_data['phone'] = input('Enter your phone: ')
    return user_data


def print_user_data(**kwargs):
    """Prints the user data in one line."""
    print(f"{kwargs['first_name']} {kwargs['last_name']} was born in {kwargs['city']}", end=' ')
    print(f"in {kwargs['birth_year']}. His e-mail address is {kwargs['email']} and phone number is {kwargs['phone']}.")


user_data = get_user_data()
print_user_data(first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                birth_year=user_data['birth_year'],
                city=user_data['city'],
                email=user_data['email'],
                phone=user_data['phone'])
