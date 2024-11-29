def are_equivalent(a, b):
    def sum_of_divisors(n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += i
        return total
    
    return sum_of_divisors(a) == sum_of_divisors(b)
assert are_equivalent(36, 57) == False
assert are_equivalent(2, 4) == False
assert are_equivalent(23, 47) == True