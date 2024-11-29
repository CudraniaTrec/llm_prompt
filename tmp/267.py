def square_Sum(n):
    total = 0
    for i in range(n):
        odd_number = 2 * i + 1
        total += odd_number ** 2
    return total
assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84