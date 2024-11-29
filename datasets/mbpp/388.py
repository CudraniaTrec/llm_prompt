#Write a python function to find the highest power of 2 that is less than or equal to n.
def highest_Power_of_2(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 