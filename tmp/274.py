def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for k in range(0, n + 1, 2):
        total_sum += binomial_coefficient(n, k)
    return total_sum

def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c
assert even_binomial_Coeff_Sum(4) == 8
assert even_binomial_Coeff_Sum(6) == 32
assert even_binomial_Coeff_Sum(2) == 2