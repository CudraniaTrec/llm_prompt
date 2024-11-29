def sum_average(n):
    total_sum = sum(range(1, n + 1))
    average = total_sum / n
    return (total_sum, average)
assert sum_average(10)==(55, 5.5)
assert sum_average(15)==(120, 8.0)
assert sum_average(20)==(210, 10.5)