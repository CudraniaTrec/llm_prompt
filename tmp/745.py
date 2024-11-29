def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        str_num = str(num)
        all_divisible = True
        for digit in str_num:
            if digit != '0' and num % int(digit) != 0:
                all_divisible = False
                break
        if all_divisible:
            result.append(num)
    return result
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
assert divisible_by_digits(20,25)==[22, 24]