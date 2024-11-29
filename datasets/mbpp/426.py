#Write a function to filter odd numbers.
def filter_oddnumbers(nums):
 odd_nums = list(filter(lambda x: x%2 != 0, nums))
 return odd_nums