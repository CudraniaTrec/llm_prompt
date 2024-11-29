def all_unique(input_list):
    return len(input_list) == len(set(input_list))
assert all_unique([1,2,3]) == True
assert all_unique([1,2,1,2]) == False
assert all_unique([1,2,3,4,5]) == True