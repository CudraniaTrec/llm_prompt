def newman_prime(n):
    if n < 1:
        return None
    
    newman_primes = []
    num = 2
    
    while len(newman_primes) < n:
        if is_newman_prime(num):
            newman_primes.append(num)
        num += 1
    
    return newman_primes[-1]

def is_newman_prime(p):
    if p < 2:
        return False
    for i in range(1, p):
        if (i ** 2 + i + 1) % p == 0:
            return False
    return True
assert newman_prime(3) == 7
assert newman_prime(4) == 17
assert newman_prime(5) == 41