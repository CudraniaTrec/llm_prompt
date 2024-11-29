def mul_even_odd(lst):
    even = None
    odd = None
    
    for number in lst:
        if number % 2 == 0 and even is None:
            even = number
        elif number % 2 != 0 and odd is None:
            odd = number
        
        if even is not None and odd is not None:
            break
    
    if even is not None and odd is not None:
        return even * odd
    return None
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
assert mul_even_odd([1,5,7,9,10])==10