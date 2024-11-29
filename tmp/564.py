def count_Pairs(lst, n):
    unique_elements = set(lst)
    count = 0
    unique_list = list(unique_elements)
    
    for i in range(len(unique_list)):
        for j in range(i + 1, len(unique_list)):
            count += 1
            
    return count
assert count_Pairs([1,2,1],3) == 2
assert count_Pairs([1,1,1,1],4) == 0
assert count_Pairs([1,2,3,4,5],5) == 10