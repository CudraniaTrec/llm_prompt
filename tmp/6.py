def differ_At_One_Bit_Pos(num1, num2):
    xor_result = num1 ^ num2
    return xor_result != 0 and (xor_result & (xor_result - 1)) == 0
assert differ_At_One_Bit_Pos(13,9) == True
assert differ_At_One_Bit_Pos(15,8) == False
assert differ_At_One_Bit_Pos(2,4) == False
assert differ_At_One_Bit_Pos(2, 3) == True
assert differ_At_One_Bit_Pos(5, 1) == True