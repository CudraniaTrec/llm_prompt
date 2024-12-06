#Write a function to interleave 3 lists of the same length into a single flat list.
def interleave_lists(list1,list2,list3):
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result