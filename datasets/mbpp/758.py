#Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
def unique_sublists(list1):
    result ={}
    for l in  list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result