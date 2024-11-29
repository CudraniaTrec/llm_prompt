def dif_Square(n):
    return n % 2 == 0 or n % 4 == 1
assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True