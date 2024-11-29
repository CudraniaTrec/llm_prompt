def check_min_heap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
assert check_min_heap([2, 10, 4, 5, 3, 15]) == False