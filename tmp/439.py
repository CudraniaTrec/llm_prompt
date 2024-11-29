def multiple_to_single(int_list):
    return int(''.join(map(str, int_list)))
assert multiple_to_single([11, 33, 50])==113350
assert multiple_to_single([-1,2,3,4,5,6])==-123456
assert multiple_to_single([10,15,20,25])==10152025