print("""
Password validation requirements:
. At least 1 uppercase Letter
. At least 1 Lowercase Letter
. At least 1 numerical number
. At least 8 characters lenght
. Limit to 3 attempts
""")

attempts = 3
while attempts > 0:
    user_password = input('Enter a password: ')
    upper = False
    lower = False
    number = False

    length = (len(user_password) >= 8)

    for i in user_password:
        if i.isupper():
            upper = True

        if i.islower():
            lower = True

        if i.isdigit():
            number = True

    if length and upper and lower and number:
        print(f'\nValid Password: {user_password}')
        break

    attempts -= 1
    if attempts <= 0:
        print('You have run out of attempts. Try again later.')
    else:
        print(f'Invalid Password. Try again. Attempts left: {attempts} ')