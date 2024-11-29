#Write a python function to remove duplicate numbers from a given number of lists.
def two_unique_nums(nums):
  return [i for i in nums if nums.count(i)==1]