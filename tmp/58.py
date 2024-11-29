def opposite_Signs(a, b):
    return (a < 0 < b) or (b < 0 < a)
assert opposite_Signs(1,-2) == True
assert opposite_Signs(3,2) == False
assert opposite_Signs(-10,-10) == False
assert opposite_Signs(-2,2) == True