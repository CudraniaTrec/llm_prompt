def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 0
assert count_divisors(10)
assert not count_divisors(100)
assert count_divisors(125)