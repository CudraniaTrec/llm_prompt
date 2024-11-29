def get_ludic(n):
    ludic_numbers = []
    sieve = [True] * (n + 1)
    for i in range(1, n + 1):
        if sieve[i]:
            ludic_numbers.append(i)
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    return ludic_numbers
assert get_ludic(10) == [1, 2, 3, 5, 7]
assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]