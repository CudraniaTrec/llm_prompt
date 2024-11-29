def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    index = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            index = mid
            right = mid - 1  # Look for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return index
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4