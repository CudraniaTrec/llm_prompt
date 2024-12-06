#Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
def sort_numeric_strings(nums_str):
    result = [int(x) for x in nums_str]
    result.sort()
    return result