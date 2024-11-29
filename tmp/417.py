def group_tuples(tuples):
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for a, b in tuples:
        groups[a].append(b)
    
    result = []
    for key, values in groups.items():
        result.append((key,) + tuple(values))
    
    return result
assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]