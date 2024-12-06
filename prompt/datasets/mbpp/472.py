#Write a python function to check whether the given list contains consecutive numbers or not.
def check_Consecutive(l): 
    return sorted(l) == list(range(min(l),max(l)+1)) 