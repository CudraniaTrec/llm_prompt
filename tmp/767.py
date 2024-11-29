def get_pairs_count(numbers, target_sum):
    count = 0
    num_dict = {}
    
    for num in numbers:
        complement = target_sum - num
        if complement in num_dict:
            count += num_dict[complement]
        
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
            
    return count
def get_pairs_count(numbers, target_sum):
    count = 0
    num_dict = {}
    
    for num in numbers:
        complement = target_sum - num
        if complement in num_dict:
            count += num_dict[complement]
        
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
            
    return count

assert get_pairs_count([1,1,1,1],2) == 6
assert get_pairs_count([1,1,1,1],2) == 6
assert get_pairs_count([1,5,7,-1,5],6) == 3
assert get_pairs_count([1,-2,3],1) == 1
assert get_pairs_count([-1,-2,3],-3) == 1