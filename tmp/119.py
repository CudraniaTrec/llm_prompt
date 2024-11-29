def search(nums):
    n = len(nums)
    if n == 0:
        return None
    for i in range(0, n, 2):
        if i == n - 1 or nums[i] != nums[i + 1]:
            return nums[i]
assert search([1,1,2,2,3]) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
assert search([1,2,2,3,3,4,4]) == 1