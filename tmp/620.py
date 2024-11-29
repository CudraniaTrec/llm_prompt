def largest_subset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
def largest_subset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
def largest_subset(nums):
    # Sort the input list to ensure that we can compare divisibility correctly
    nums.sort()
    # Get the length of the sorted list
    n = len(nums)
    # Create a dynamic programming list initialized to 1
    dp = [1] * n
    
    # Iterate through each number in the list starting from the second element
    for i in range(1, n):
        # Compare the current number with all previous numbers
        for j in range(i):
            # Check if the current number is divisible by the previous number
            if nums[i] % nums[j] == 0:
                # Update the dp array with the maximum subset size at index i
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum value from the dp array, which indicates the size of the largest subset
    return max(dp)

assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
assert largest_subset([10, 5, 3, 15, 20]) == 3
assert largest_subset([18, 1, 3, 6, 13, 17]) == 4