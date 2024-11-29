def diff_even_odd(lst):
    even = None
    odd = None
    
    for num in lst:
        if num % 2 == 0 and even is None:
            even = num
        elif num % 2 != 0 and odd is None:
            odd = num
        
        if even is not None and odd is not None:
            break
    
    return even - odd if even is not None and odd is not None else None
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
assert diff_even_odd([1,5,7,9,10])==9