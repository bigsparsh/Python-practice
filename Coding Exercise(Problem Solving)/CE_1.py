num_of_tries = 0
num_of_heads = 0

while True:
    flip_result = input('Throw the coin and enter head or tail here: ')
    num_of_tries += 1

    match flip_result.capitalize():
        case 'Head':
            num_of_heads += 1

    print(f'Head: {float(num_of_heads * 100 / num_of_tries)}%')

    with open('probability.txt') as file:
        result = file.readlines()
    result.append(flip_result)

    result = [i + '\n' for i in result]

    with open('probability.txt', 'w') as file:
        file.writelines(result)
