#Write a function to count the number of lists within a list. The function should return a dictionary, where every list is turned to a tuple, and the value of the tuple is the number of its occurrences.
def unique_sublists(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result