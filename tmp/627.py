def find_First_Missing(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] != i:
            return i
    return n
assert find_First_Missing([0,1,2,3]) == 4
assert find_First_Missing([0,1,2,6,9]) == 3
assert find_First_Missing([2,3,5,8,9]) == 0