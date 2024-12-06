#Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
import math 
def find_Index(n): 
    x = math.sqrt(2 * math.pow(10,(n - 1)))
    return round(x)