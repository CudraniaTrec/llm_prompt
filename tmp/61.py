def count_Substrings(s):
    count = 0
    n = len(s)
    
    for start in range(n):
        digit_sum = 0
        
        for end in range(start, n):
            digit_sum += int(s[end])
            length = end - start + 1
            
            if digit_sum == length:
                count += 1
                
    return count
def count_Substrings(s):
    count = 0
    n = len(s)
    
    for start in range(n):
        digit_sum = 0
        
        for end in range(start, n):
            digit_sum += int(s[end])
            length = end - start + 1
            
            if digit_sum == length:
                count += 1
                
    return count

assert count_Substrings('112112') == 6
assert count_Substrings('112112') == 6
assert count_Substrings('111') == 6
assert count_Substrings('1101112') == 12