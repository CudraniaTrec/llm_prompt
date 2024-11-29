def odd_Equivalent(binary_string, rotations):
    odd_count = 0
    length = len(binary_string)

    for i in range(rotations):
        rotated = binary_string[i % length]
        if rotated == '1':
            odd_count += 1

    return odd_count
def odd_Equivalent(binary_string, rotations):
    odd_count = 0
    length = len(binary_string)

    for i in range(rotations):
        rotated = binary_string[i % length]
        if rotated == '1':
            odd_count += 1

    return odd_count

assert odd_Equivalent("011001",6) == 3
def odd_Equivalent(binary_string, rotations):
    odd_count = 0
    length = len(binary_string)

    for i in range(rotations):
        rotated = binary_string[i % length]
        if rotated == '1':
            odd_count += 1

    return odd_count

assert odd_Equivalent("011001",6) == 3
assert odd_Equivalent("011001",6) == 3
assert odd_Equivalent("11011",5) == 4
assert odd_Equivalent("1010",4) == 2