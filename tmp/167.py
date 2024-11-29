def next_power_of_2(n):
    if n <= 0:
        return 1
    power = 1
    while power < n:
        power *= 2
    return power
assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(17) == 32