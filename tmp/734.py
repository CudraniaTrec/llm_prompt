def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            total_sum += product
    return total_sum
assert sum_Of_Subarray_Prod([1,2,3]) == 20
assert sum_Of_Subarray_Prod([1,2]) == 5
assert sum_Of_Subarray_Prod([1,2,3,4]) == 84