def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
assert prime_num(13)==True
assert prime_num(7)==True
assert prime_num(-1010)==False