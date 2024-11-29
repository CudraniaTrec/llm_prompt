def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    while n > 0:
        if n & 1:  # Check if the least significant bit is 1
            n -= 1  # Decrement by 1
        else:
            n >>= 1  # Right shift n to check the next bit
    return True
assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(7) == False
assert is_Sum_Of_Powers_Of_Two(14) == True