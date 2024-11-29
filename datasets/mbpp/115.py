#Write a function to check whether all dictionaries in a list are empty or not.
def empty_dit(list1):
 empty_dit=all(not d for d in list1)
 return empty_dit