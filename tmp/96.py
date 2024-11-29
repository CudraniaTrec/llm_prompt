def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
assert divisor(15) == 4
assert divisor(12) == 6
assert divisor(9) == 3