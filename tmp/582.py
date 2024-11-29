def my_dict(d):
    return len(d) == 0
assert my_dict({10})==False
assert my_dict({11})==False
assert my_dict({})==True