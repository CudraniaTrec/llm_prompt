def check_Consecutive(nums):
    if not nums:
        return False
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i] + 1 != nums_sorted[i + 1]:
            return False
    return True
def check_Consecutive(nums):
    if not nums:
        return False
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i] + 1 != nums_sorted[i + 1]:
            return False
    return True

assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,5]) == False
assert check_Consecutive([3,4,5,6]) == True
assert check_Consecutive([]) == False
assert check_Consecutive([10]) == True
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,5,6]) == False
assert check_Consecutive([1,2,1]) == False