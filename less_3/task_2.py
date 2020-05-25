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


def get_user_birth_year():
    """Returns a year of birth entered by the user.

    () -> (whole number)

    >>> get_user_birth_year()
    1990
    """
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


def get_user_data():
    """Returns a dictionary of user data.

    () -> user_data_template

    >>> get_user_data()
    {'first_name': 'Denis',
     'last_name': 'Borisov',
     'birth_year': 1990,
     'city': 'Moscow',
     'email': 'd****.******v@h******.com',
     'phone': '8***725****',
    }
    """
    user_data = {}
    user_data['first_name'] = input('Enter your first name: ')
    user_data['last_name'] = input('Enter your last name: ')
    user_data['birth_year'] = get_user_birth_year()
    user_data['city'] = input('Enter your city: ')
    user_data['email'] = input('Enter your email: ')
    user_data['phone'] = input('Enter your phone: ')
    return user_data


def print_user_data(first_name, last_name, birth_year, city, email, phone):
    """Prints the user data in one line.

    (string, string, number, string, string, string) -> (whole number)
    """
    print(f'{first_name} {last_name} was born in {city} in {birth_year}.', end=' ')
    print(f'His e-mail address is {email} and phone number is {phone}.')


user_data = get_user_data()
print_user_data(first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                birth_year=user_data['birth_year'],
                city=user_data['city'],
                email=user_data['email'],
                phone=user_data['phone'])
