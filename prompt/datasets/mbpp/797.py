#Write a python function to find the sum of all odd natural numbers within the range l and r.
def sum_odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_range(l,r): 
    return sum_odd(r) - sum_odd(l - 1)