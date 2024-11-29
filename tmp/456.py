def reverse_string_list(string_list):
    return [s[::-1] for s in string_list]
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']