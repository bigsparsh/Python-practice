waiting_list = ['John', 'Mary']
name = input('Enter name: ')
try:
    number = waiting_list.index(name)
except ValueError:
    exit(f'{name} is not in the list.')
print(f"{name}'s turn is {number}.")