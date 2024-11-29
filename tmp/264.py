def dog_age(human_years):
    return human_years * 7
def dog_age(human_years):
    if human_years == 1:
        return 15
    elif human_years == 2:
        return 24
    else:
        return 24 + (human_years - 2) * 5
def dog_age(human_years):
    if human_years < 0:
        return "Invalid age"
    elif human_years == 1:
        return 15
    elif human_years == 2:
        return 24
    else:
        return 24 + (human_years - 2) * 5
assert dog_age(12)==61
assert dog_age(15)==73
assert dog_age(24)==109