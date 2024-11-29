def return_sum(input_dict):
    total = 0
    for value in input_dict.values():
        total += value
    return total
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
assert return_sum({'a': 36, 'b':39, 'c':49}) == 124