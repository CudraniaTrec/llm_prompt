#Write a function to compute the n-th power of each number in a list.
def nth_nums(nums,n):
 nth_nums = list(map(lambda x: x ** n, nums))
 return nth_nums