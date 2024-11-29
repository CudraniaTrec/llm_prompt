def kth_element(arr, k):
    arr.sort()
    return arr[k - 1]
def kth_element(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the array")
    arr.sort()
    return arr[k - 1]
def kth_element(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the array")
    arr.sort()
    return arr[k - 1]
def kth_element(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the array")
    arr.sort()
    return arr[k - 1]
assert kth_element([12,3,5,7,19], 2) == 3
assert kth_element([17,24,8,23], 3) == 8
assert kth_element([16,21,25,36,4], 4) == 36