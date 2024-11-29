def remove_lowercase(s):
    result = ''.join([char for char in s if not char.islower()])
    return result
def remove_lowercase(s):
    result = ''.join([char for char in s if not char.islower()])
    return result

assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("FInD")==('FID')
assert remove_lowercase("STRinG")==('STRG')