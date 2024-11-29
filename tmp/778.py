def pack_consecutive_duplicates(input_list):
    if not input_list:
        return []
    
    packed_list = []
    current_pack = [input_list[0]]
    
    for item in input_list[1:]:
        if item == current_pack[-1]:
            current_pack.append(item)
        else:
            packed_list.append(current_pack)
            current_pack = [item]
    
    packed_list.append(current_pack)
    return packed_list
def pack_consecutive_duplicates(input_list):
    if not input_list:
        return []
    
    packed_list = []
    current_pack = [input_list[0]]
    
    for item in input_list[1:]:
        if item == current_pack[-1]:
            current_pack.append(item)
        else:
            packed_list.append(current_pack)
            current_pack = [item]
    
    packed_list.append(current_pack)
    return packed_list

assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]