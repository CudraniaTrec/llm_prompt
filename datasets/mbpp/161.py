#Write a function to remove all elements from a given list present in another list.
def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result