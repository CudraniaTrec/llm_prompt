def even_Power_Sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        total_sum += even_number ** 5
    return total_sum
assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32