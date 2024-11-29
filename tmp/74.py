def is_samepatterns(patterns, values):
    if len(patterns) != len(values):
        return False
    
    pattern_to_value = {}
    value_to_pattern = {}
    
    for pattern, value in zip(patterns, values):
        if pattern in pattern_to_value:
            if pattern_to_value[pattern] != value:
                return False
        else:
            pattern_to_value[pattern] = value
        
        if value in value_to_pattern:
            if value_to_pattern[value] != pattern:
                return False
        else:
            value_to_pattern[value] = pattern
    
    return True
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
assert is_samepatterns(["red","green","greenn"], ["a","b"])==False