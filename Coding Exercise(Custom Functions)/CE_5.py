def get_num_of_people(people_local):
    num_of_ppl = len(people_local.split(','))
    return num_of_ppl


people = input('Enter names separated by commas (no spaces): ')
number_of_people = get_num_of_people(people)
print(f'There are {number_of_people} people present.')