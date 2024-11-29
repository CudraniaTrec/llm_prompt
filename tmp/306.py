def max_sum_increasing_subseq(arr, n, i, k):
    max_sum = [0] * n
    for j in range(i + 1):
        max_sum[j] = arr[j] if j == 0 else max(max_sum[j - 1], max_sum[j] + arr[j])
    
    total = 0
    for j in range(i + 1):
        if arr[j] < arr[k]:
            total = max(total, max_sum[j])
    
    return total + arr[k]

assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
def max_sum_increasing_subseq(arr, n, i, k):
    max_sum = [0] * n
    for j in range(i + 1):
        if j == 0:
            max_sum[j] = arr[j]
        else:
            max_sum[j] = max(max_sum[j - 1], max_sum[j - 1] if arr[j] > arr[j - 1] else 0) + arr[j]
    
    total = 0
    for j in range(i + 1):
        if arr[j] < arr[k]:
            total = max(total, max_sum[j])
    
    return total + arr[k]

assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71