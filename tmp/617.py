def min_Jumps(destination, jump_length):
    d, h = destination
    import math
    horizontal_jumps = d / jump_length
    total_jumps = math.sqrt(horizontal_jumps**2 + (h / jump_length)**2)
    return total_jumps
assert min_Jumps((3,4),11)==3.5
assert min_Jumps((3,4),0)==0
assert min_Jumps((11,14),11)==1