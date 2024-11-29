def count_occurance(input_string):
    return input_string.count('std')
assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("truststdsolensporsd") == 1
assert count_occurance("makestdsostdworthit") == 2
assert count_occurance("stds") == 1
assert count_occurance("") == 0