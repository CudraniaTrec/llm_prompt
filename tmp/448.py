def cal_sum(n):
    perrin = [3, 0, 2]
    if n < 3:
        return perrin[n]
    
    total_sum = sum(perrin)
    for i in range(3, n + 1):
        next_perrin = perrin[i - 2] + perrin[i - 1]
        perrin.append(next_perrin)
        total_sum += next_perrin
    
    return total_sum
def cal_sum(n):
    perrin = [3, 0, 2]
    if n == 0:
        return perrin[0]
    elif n == 1:
        return perrin[1]
    elif n == 2:
        return perrin[2]
    
    total_sum = sum(perrin)
    for i in range(3, n + 1):
        next_perrin = perrin[i - 2] + perrin[i - 1]
        perrin.append(next_perrin)
        total_sum += next_perrin
    
    return total_sum
assert cal_sum(9) == 49
assert cal_sum(10) == 66
assert cal_sum(11) == 88