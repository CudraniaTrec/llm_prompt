#Write a python function to check if a given number is one less than twice its reverse.
def rev(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def check(n):    
    return (2 * rev(n) == n + 1)  