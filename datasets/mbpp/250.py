#Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
def count_X(tup, x): 
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count 