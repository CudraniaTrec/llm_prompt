def dict_depth(d):
    if isinstance(d, dict) and d:
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
def dict_depth(d):
    if isinstance(d, dict) and d:
        return 1 + max(dict_depth(v) for v in d.values())
    return 1 if isinstance(d, dict) else 0
def dict_depth(d):
    if isinstance(d, dict) and d:
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
def dict_depth(d):
    if isinstance(d, dict) and d:
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
def dict_depth(d):
    if isinstance(d, dict) and d:
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
def dict_depth(d):
    if isinstance(d, dict) and d:
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
def dict_depth(d):
    if isinstance(d, dict):
        if d:
            return 1 + max(dict_depth(v) for v in d.values())
        return 1
    return 0
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c':'python'}})==2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3