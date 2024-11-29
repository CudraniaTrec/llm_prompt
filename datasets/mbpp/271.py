#Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
def even_Power_Sum(n): 
    sum = 0; 
    for i in range(1,n+1): 
        j = 2*i; 
        sum = sum + (j*j*j*j*j); 
    return sum; 