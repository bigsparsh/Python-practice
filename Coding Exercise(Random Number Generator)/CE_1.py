import random


def random_generator(lower_bound_local, upper_bound_local):
    rand_num = random.randrange(lower_bound_local, upper_bound_local + 1)
    return rand_num


lower_bound = int(input('Enter the lower bound: '))
upper_bound = int(input('Enter the upper bound: '))

print(random_generator(lower_bound, upper_bound))