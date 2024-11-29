def count_reverse_pairs(string_list):
    count = 0
    seen = set()
    
    for string in string_list:
        reverse_string = string[::-1]
        if reverse_string in seen:
            count += 1
        seen.add(string)
        
    return count
def count_reverse_pairs(string_list):
    count = 0
    seen = set()
    
    for string in string_list:
        reverse_string = string[::-1]
        if reverse_string in seen:
            count += 1
        seen.add(string)
        
    return count

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
def count_reverse_pairs(string_list):
    count = 0
    seen = set()
    
    for string in string_list:
        reverse_string = string[::-1]
        if reverse_string in seen:
            count += 1
        seen.add(string)
        
    return count

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2