#Write a python function to check whether a list of numbers contains only one distinct element or not.
def unique_Element(arr):
    s = set(arr)
    return len(s) == 1