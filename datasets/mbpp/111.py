#Write a function to find the common elements in given nested lists.
def common_in_nested_lists(nestedlist):
    result = list(set.intersection(*map(set, nestedlist)))
    return result