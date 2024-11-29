def remove_dirty_chars(str1, str2):
    return ''.join(char for char in str1 if char not in str2)
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'