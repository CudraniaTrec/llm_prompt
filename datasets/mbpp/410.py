#Write a function to find the minimum value in a given heterogeneous list.
def min_val(listval):
     min_val = min(i for i in listval if isinstance(i, int))
     return min_val