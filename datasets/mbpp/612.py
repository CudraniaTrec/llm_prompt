#Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
def merge(lst):  
    return [list(ele) for ele in list(zip(*lst))] 