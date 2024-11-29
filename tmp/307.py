def colon_tuplex(tup, index, value):
    tup_as_list = list(tup)
    tup_as_list[index] = value
    return tuple(tup_as_list)
assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)