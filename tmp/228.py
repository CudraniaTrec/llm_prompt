def all_Bits_Set_In_The_Given_Range(num, start, end):
    mask = ((1 << (end - start + 1)) - 1) << start
    return (num & mask) == 0
assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
assert all_Bits_Set_In_The_Given_Range(39,4,6) == False