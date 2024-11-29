def text_lowercase_underscore(s):
    import re
    return bool(re.match(r'^[a-z]+(_[a-z]+)*$', s))
assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("aab_Abbbc")==(False)
assert text_lowercase_underscore("Aaab_abbbc")==(False)