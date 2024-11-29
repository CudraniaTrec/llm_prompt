def sum_div(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
assert sum_div(8)==7
assert sum_div(12)==16
assert sum_div(7)==1