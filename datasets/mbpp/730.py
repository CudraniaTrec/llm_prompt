#Write a function to remove consecutive duplicates of a given list.
from itertools import groupby
def consecutive_duplicates(nums):
    return [key for key, group in groupby(nums)] 