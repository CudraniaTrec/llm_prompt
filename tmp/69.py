def is_sublist(main_list, sub_list):
    sub_len = len(sub_list)
    main_len = len(main_list)
    
    if sub_len == 0:
        return True
    
    for i in range(main_len - sub_len + 1):
        if main_list[i:i + sub_len] == sub_list:
            return True
            
    return False
assert is_sublist([2,4,3,5,7],[3,7])==False
assert is_sublist([2,4,3,5,7],[4,3])==True
assert is_sublist([2,4,3,5,7],[1,6])==False