#Write a python function to find the first digit of a given number.
def first_Digit(n) :  
    while n >= 10:  
        n = n / 10 
    return int(n) 