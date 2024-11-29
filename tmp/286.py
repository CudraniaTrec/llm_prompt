def max_sub_array_sum_repeated(arr, n, k):
    if k == 0 or n == 0:
        return 0
    if k == 1:
        return max_sub_array_sum(arr)
    
    total_sum = sum(arr)
    max_sum = max_sub_array_sum(arr)
    
    if total_sum > 0:
        return max(max_sum, max_sum + (k - 1) * total_sum)
    else:
        return max(max_sum, max_sum + total_sum * (k - 1), max_sub_array_sum(arr[:n*2]))

def max_sub_array_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1