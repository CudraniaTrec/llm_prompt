#Write a function to sort each sublist of strings in a given list of lists.
def sort_sublists(list1):
    result = list(map(sorted,list1)) 
    return result