def highest_Power_of_2(n):
    power = 1
    while power <= n:
        power *= 2
    return power // 2
assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32