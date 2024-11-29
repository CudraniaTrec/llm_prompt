def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
            
    return max_sum
def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10