def neg_nos(lst):
    return [num for num in lst if num < 0]
assert neg_nos([-1,4,5,-6]) == [-1,-6]
assert neg_nos([-1,-2,3,4]) == [-1,-2]
assert neg_nos([-7,-6,8,9]) == [-7,-6]