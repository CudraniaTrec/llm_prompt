def even_bit_set_number(n):
    mask = 0b1010101010101010101010101010101010101010101010101010101010101010
    return n | mask
def even_bit_set_number(n):
    mask = 0b1010101010101010101010101010101010101010101010101010101010101010
    return n & ~mask
assert even_bit_set_number(10) == 10
assert even_bit_set_number(20) == 30
assert even_bit_set_number(30) == 30