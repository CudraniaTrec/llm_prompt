#Write a function to sort each sublist of strings in a given list of lists.
def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result
