def Find_Min(lst):
    min_length = float('inf')
    min_sublist = []
    
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
            
    return min_sublist
def Find_Min(lst):
    min_length = float('inf')
    min_sublist = []
    
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
            
    return min_sublist

assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']