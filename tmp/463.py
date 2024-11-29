def max_subarray_product(arr):
    max_product = arr[0]
    current_product = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] == 0:
            current_product = 1
            continue
        
        current_product *= arr[i]
        max_product = max(max_product, current_product)
        
        # Reset current_product if it becomes negative
        if current_product < 0:
            current_product = 1
            
    return max_product
def max_subarray_product(arr):
    if not arr:
        return 0
    
    max_product = arr[0]
    current_product = arr[0]
    temp_product = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] == 0:
            current_product = 1
            temp_product = 1
            continue
        
        current_product *= arr[i]
        temp_product *= arr[i]
        
        if temp_product < 0:
            temp_product = 1
        
        max_product = max(max_product, current_product, temp_product)
        
    return max_product
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
assert max_subarray_product([6, -3, -10, 0, 2]) == 180
assert max_subarray_product([-2, -40, 0, -2, -3]) == 80