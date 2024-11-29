def max_aggregate(tuples_list):
    aggregate = {}
    for name, score in tuples_list:
        if name in aggregate:
            aggregate[name] += score
        else:
            aggregate[name] = score
    max_name = max(aggregate, key=aggregate.get)
    return (max_name, aggregate[max_name])
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)