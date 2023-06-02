boiling_point = 100
freezing_point = 0


def state_of_water(temperature_local):
    if temperature_local >= boiling_point:
        return 'Gas'
    elif freezing_point < temperature_local < boiling_point:
        return 'Liquid'
    else:
        return 'Solid'
