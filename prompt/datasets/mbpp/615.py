#Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result