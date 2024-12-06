#Write a python function to check whether every odd index contains odd numbers of a given list.
def odd_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))