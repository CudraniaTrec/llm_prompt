def find_length(s):
    max_diff = 0
    current_diff = 0
    
    for char in s:
        if char == '0':
            current_diff += 1
        else:
            current_diff -= 1
        
        max_diff = max(max_diff, current_diff)
        
        if current_diff < 0:
            current_diff = 0
            
    return max_diff
def find_length(s):
    max_diff = 0
    current_diff = 0
    
    for char in s:
        if char == '0':
            current_diff += 1
        else:
            current_diff -= 1
        
        max_diff = max(max_diff, current_diff)
        
        if current_diff < 0:
            current_diff = 0
            
    return max_diff

assert find_length("11000010001") == 6
assert find_length("11000010001") == 6
assert find_length("10111") == 1
assert find_length("11011101100101") == 2