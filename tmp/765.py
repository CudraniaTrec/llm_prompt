def is_polite(n):
    polite_count = 0
    num = 1
    while polite_count < n:
        if num & (num - 1) != 0:  # Check if num is not a power of 2
            polite_count += 1
        if polite_count < n:
            num += 1
    return num
assert is_polite(7) == 11
assert is_polite(4) == 7
assert is_polite(9) == 13