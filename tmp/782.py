def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for length in range(1, n + 1, 2):  # Only odd lengths
            if i + length <= n:  # Check if subarray is within bounds
                total_sum += sum(arr[i:i + length])
    return total_sum
assert odd_length_sum([1,2,4]) == 14
assert odd_length_sum([1,2,1,2]) == 15
assert odd_length_sum([1,7]) == 8