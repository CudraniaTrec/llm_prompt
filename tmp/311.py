def set_left_most_unset_bit(n):
    # Find the position of the left most unset bit
    position = 0
    while (1 << position) <= n:
        position += 1
    
    # Set that bit in the original number
    result = n | (1 << position)
    return result
def set_left_most_unset_bit(n):
    # Find the position of the left most unset bit
    position = 0
    while (1 << position) <= n:
        position += 1
        
    # Check for the left most unset bit in the number
    while (1 << position) & n:
        position -= 1
    
    # Set that bit in the original number
    result = n | (1 << position)
    return result
assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15