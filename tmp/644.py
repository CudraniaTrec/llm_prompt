def reverse_Array_Upto_K(arr, k):
    if k > len(arr) or k < 1:
        return arr
    reversed_part = arr[:k][::-1]
    return reversed_part + arr[k:]
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]