def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
assert even_position([3,2,1]) == False
assert even_position([1,2,3]) == False
assert even_position([2,1,4]) == True