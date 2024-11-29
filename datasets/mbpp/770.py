#Write a python function to find the sum of fourth power of first n odd natural numbers.
def odd_num_sum(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 