from itertools import product

def find_combinations(tuple_list):
    all_combinations = product(*tuple_list)
    sum_combinations = set()
    
    for combination in all_combinations:
        sum_tuple = (sum(combination[i] for i in range(len(combination))), 
                     sum(combination[i] for i in range(len(combination) - 1, -1, -1)))
        sum_combinations.add(sum_tuple)
    
    return sorted(list(sum_combinations))
from itertools import product

def find_combinations(tuple_list):
    all_combinations = product(*tuple_list)
    sum_combinations = set()
    
    for combination in all_combinations:
        sum_tuple = (sum(combination), sum(combination[::-1]))
        sum_combinations.add(sum_tuple)
    
    return sorted(list(sum_combinations))
from itertools import product

def find_combinations(tuple_list):
    all_combinations = product(*tuple_list)
    sum_combinations = set()
    
    for combination in all_combinations:
        sum_tuple = (sum(combination), sum(combination[::-1]))
        sum_combinations.add(sum_tuple)
    
    return sorted(list(sum_combinations))

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]