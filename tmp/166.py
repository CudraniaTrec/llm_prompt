def find_even_pair(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
    return count
assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
assert find_even_pair([1, 2, 3]) == 1