def find_solution(a, b, n):
    for x in range(n // a + 1):
        for y in range(n // b + 1):
            if a * x + b * y == n:
                return (x, y)
    return None
assert find_solution(2, 3, 7) == (2, 1)
assert find_solution(4, 2, 7) == None
assert find_solution(1, 13, 17) == (4, 1)