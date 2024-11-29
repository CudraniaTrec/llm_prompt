def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
    return sum(primes)
assert count_Primes_nums(5) == 2
assert count_Primes_nums(10) == 4
assert count_Primes_nums(100) == 25