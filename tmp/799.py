def left_rotate(num, d):
    d = d % 32
    return ((num << d) | (num >> (32 - d))) & 0xFFFFFFFF
assert left_rotate(16,2) == 64
assert left_rotate(10,2) == 40
assert left_rotate(99,3) == 792
assert left_rotate(99,3) == 792
assert left_rotate(0b0001,3) == 0b1000