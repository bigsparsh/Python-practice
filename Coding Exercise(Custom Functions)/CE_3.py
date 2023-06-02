def check_password(password):
    pass_characters = len(password)
    uppercase_letter = False
    digit_availability = False
    for i in password:
        if i.isdigit():
            digit_availability = True
        if i.isupper():
            uppercase_letter = True

    password_eligibility = []
    if pass_characters >= 8:
        password_eligibility.append(True)
    else:
        password_eligibility.append(False)
    if uppercase_letter:
        password_eligibility.append(True)
    else:
        password_eligibility.append(False)
    if digit_availability:
        password_eligibility.append(True)
    else:
        password_eligibility.append(False)

    if all(password_eligibility):
        return 'Strong Password'
    else:
        return 'Weak Password'


user_password = input('Enter a password: ')
print(check_password(user_password))