def find_Index(n):
    index = 0
    triangular_number = 0
    while True:
        index += 1
        triangular_number = index * (index + 1) // 2
        if len(str(triangular_number)) >= n:
            return index
assert find_Index(2) == 4
assert find_Index(3) == 14
assert find_Index(4) == 45