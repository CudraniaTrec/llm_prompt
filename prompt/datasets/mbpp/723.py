#The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result