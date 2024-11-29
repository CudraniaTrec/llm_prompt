def number_ctr(input_string):
    count = 0
    for char in input_string:
        if char.isdigit():
            count += 1
    return count
assert number_ctr('program2bedone') == 1
assert number_ctr('3wonders') == 1
assert number_ctr('123') == 3
assert number_ctr('3wond-1ers2') == 3