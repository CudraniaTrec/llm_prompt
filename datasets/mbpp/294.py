#Write a function to find the maximum value in a given heterogeneous list.
def max_val(listval):
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val)