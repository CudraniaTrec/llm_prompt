#Write a function to find squares of individual elements in a list.
def square_nums(nums):
 square_nums = list(map(lambda x: x ** 2, nums))
 return square_nums