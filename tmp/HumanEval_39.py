def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def prime_fib(n: int):
    fib_gen = fibonacci_generator()
    prime_fibs = []
    
    while len(prime_fibs) < n:
        fib_num = next(fib_gen)
        if is_prime(fib_num):
            prime_fibs.append(fib_num)
    
    return prime_fibs[-1]
    fib_gen = fibonacci_generator()
    prime_fibs = []
    while len(prime_fibs) < n:
        fib_num = next(fib_gen)
        if is_prime(fib_num):
            prime_fibs.append(fib_num)
    return prime_fibs[-1]


METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89


check(prime_fib)