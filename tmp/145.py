def max_Abs_Diff(arr):
    max_val = max(arr)
    min_val = min(arr)
    return max_val - min_val
assert max_Abs_Diff((2,1,5,3)) == 4
assert max_Abs_Diff((9,3,2,5,1)) == 8
assert max_Abs_Diff((3,2,1)) == 2