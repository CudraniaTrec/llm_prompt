def toggle_middle_bits(n):
    if n < 4:
        return n
    first_bit = n & 1
    last_bit = n & (1 << (n.bit_length() - 1))
    middle_bits = n >> 1 & ~(1 | (1 << (n.bit_length() - 2)))
    toggled_middle_bits = ~middle_bits & ((1 << (n.bit_length() - 2)) - 1)
    return first_bit | (toggled_middle_bits << 1) | last_bit
assert toggle_middle_bits(9) == 15
assert toggle_middle_bits(10) == 12
assert toggle_middle_bits(11) == 13
assert toggle_middle_bits(0b1000001) == 0b1111111
assert toggle_middle_bits(0b1001101) == 0b1110011