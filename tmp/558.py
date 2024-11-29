def digit_distance_nums(num1, num2):
    # Convert the numbers to strings to iterate through each digit
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Pad the shorter number with leading zeros
    max_len = max(len(str_num1), len(str_num2))
    str_num1 = str_num1.zfill(max_len)
    str_num2 = str_num2.zfill(max_len)

    # Calculate the sum of per-digit differences
    total_difference = sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str_num1, str_num2))

    return total_difference
assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(23,56) == 6
assert digit_distance_nums(123,256) == 7