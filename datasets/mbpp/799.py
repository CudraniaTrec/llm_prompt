#Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
def left_rotate(n,d):   
    INT_BITS = 32
    return (n << d)|(n >> (INT_BITS - d))  