def median_numbers(a, b, c):
    nums = [a, b, c]
    nums.sort()
    return float(nums[1])
assert median_numbers(25,55,65)==55.0
assert median_numbers(20,10,30)==20.0
assert median_numbers(15,45,75)==45.0