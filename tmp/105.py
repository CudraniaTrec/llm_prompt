def count(bool_list):
    return sum(1 for value in bool_list if value is True)
assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3