#Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
def remove_kth_element(list1, L):
    return  list1[:L-1] + list1[L:]