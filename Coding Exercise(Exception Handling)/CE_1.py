try:
    total_value = float(input('Enter total value: '))
    if total_value == 0:
        exit('Your total value cannot be zero')
    value = float(input('Enter value: '))

except ValueError:
    exit('You need to enter a number. Run the program again.')

print(f'That is {value * 100 / total_value}%')
