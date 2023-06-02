def calculate_age(year_of_birth, current_year = 2023):
    return current_year - year_of_birth


user_birth_year = int(input('Enter your year of birth: '))
user_age = calculate_age(user_birth_year)

print(f'You are {user_age} years old.')

if user_age > 120:
    print('You really lived a long life. Congrats!')
