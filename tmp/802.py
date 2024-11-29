def count_rotation(arr):
    n = len(arr)
    if n == 0:
        return 0
    low, high = 0, n - 1
    
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        
        next_mid = (mid + 1) % n
        prev_mid = (mid - 1 + n) % n
        
        if arr[mid] <= arr[next_mid] and arr[mid] <= arr[prev_mid]:
            return mid
        
        if arr[mid] <= arr[high]:
            high = mid - 1
        else:
            low = mid + 1
            
    return 0
assert count_rotation([3,2,1]) == 1
assert count_rotation([4,5,1,2,3]) == 2
assert count_rotation([7,8,9,1,2,3]) == 3
assert count_rotation([1,2,3]) == 0
assert count_rotation([1,3,2]) == 2