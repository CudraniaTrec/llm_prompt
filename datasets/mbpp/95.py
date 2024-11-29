#Write a python function to find the length of the smallest list in a list of lists.
def Find_Min_Length(lst):  
    minLength = min(len(x) for x in lst )
    return minLength 