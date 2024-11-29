#Write a python function to find the largest negative number from the given list.
def largest_neg(list1): 
    max = list1[0] 
    for x in list1: 
        if x < max : 
             max = x  
    return max