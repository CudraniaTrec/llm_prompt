def sum_of_common_divisors(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    common_divisor_sum = 0
    common_gcd = gcd(a, b)

    for i in range(1, common_gcd + 1):
        if common_gcd % i == 0:
            common_divisor_sum += i

    return common_divisor_sum
assert sum(10,15) == 6
assert sum(100,150) == 93
assert sum(4,6) == 3