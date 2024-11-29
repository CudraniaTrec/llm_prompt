def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in count_dict:
            count_dict[tuple_sublist] += 1
        else:
            count_dict[tuple_sublist] = 1
    return count_dict
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
assert unique_sublists([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]])=={(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}
assert unique_sublists([['john']])=={('john',): 1}