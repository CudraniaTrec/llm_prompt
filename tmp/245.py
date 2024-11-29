def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize the max_sum array where max_sum[i] will store the maximum sum of bitonic subsequence ending at index i
    max_sum_inc = [0] * n
    max_sum_dec = [0] * n

    # Fill the max_sum_inc array
    for i in range(n):
        max_sum_inc[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                max_sum_inc[i] = max(max_sum_inc[i], max_sum_inc[j] + arr[i])

    # Fill the max_sum_dec array
    for i in range(n-1, -1, -1):
        max_sum_dec[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[j] < arr[i]:
                max_sum_dec[i] = max(max_sum_dec[i], max_sum_dec[j] + arr[i])

    # Calculate the maximum sum of bitonic subsequence
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, max_sum_inc[i] + max_sum_dec[i] - arr[i])

    return max_bitonic_sum
def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize the max_sum array where max_sum[i] will store the maximum sum of bitonic subsequence ending at index i
    max_sum_inc = [0] * n
    max_sum_dec = [0] * n

    # Fill the max_sum_inc array
    for i in range(n):
        max_sum_inc[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                max_sum_inc[i] = max(max_sum_inc[i], max_sum_inc[j] + arr[i])

    # Fill the max_sum_dec array
    for i in range(n-1, -1, -1):
        max_sum_dec[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[j] < arr[i]:
                max_sum_dec[i] = max(max_sum_dec[i], max_sum_dec[j] + arr[i])

    # Calculate the maximum sum of bitonic subsequence
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, max_sum_inc[i] + max_sum_dec[i] - arr[i])

    return max_bitonic_sum

assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([80, 60, 30, 40, 20, 10]) == 210
assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138