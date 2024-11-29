#Write a python function to interchange the first and last elements in a list.
def swap_List(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp  
    return newList 