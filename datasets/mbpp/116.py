#Write a function to convert a given tuple of positive integers into a single integer.
def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result