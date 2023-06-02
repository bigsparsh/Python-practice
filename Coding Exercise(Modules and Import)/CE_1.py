import state_of_water_func

temperature = float(input('Enter water temperature: '))
print(f'The water is in the physical state of: {state_of_water_func.state_of_water(temperature)}')