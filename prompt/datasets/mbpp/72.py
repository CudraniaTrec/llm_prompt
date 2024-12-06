#Write a python function to check whether the given number can be represented as the difference of two squares or not.
def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False