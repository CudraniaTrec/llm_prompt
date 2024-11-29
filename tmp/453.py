def sumofFactors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            total += i
    return total
assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8