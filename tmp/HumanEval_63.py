def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    
    fibfib_values = [0, 0, 1] + [0] * (n - 2)
    
    for i in range(3, n + 1):
        fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]
    
    return fibfib_values[n]
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b, c = 0, 0, 1
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c
        
    return c
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    fibfib_values = [0, 0, 1] + [0] * (n - 2)
    for i in range(3, n + 1):
        fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]
    return fibfib_values[n]


METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81


check(fibfib)