def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_prod = [0] * n
    max_prod[0] = arr[0]

    for i in range(1, n):
        max_prod[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                max_prod[i] = max(max_prod[i], max_prod[j] * arr[i])
    
    return max(max_prod)
def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_prod = [0] * n
    max_prod[0] = arr[0]

    for i in range(1, n):
        max_prod[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                max_prod[i] = max(max_prod[i], max_prod[j] * arr[i])
    
    return max(max_prod)

assert max_product([3, 100, 4, 5, 150, 6]) == 3000
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
assert max_product([4, 42, 55, 68, 80]) == 50265600
assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460