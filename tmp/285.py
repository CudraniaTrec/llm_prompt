def text_match_two_three(string):
    import re
    pattern = r'a(b{2,3})'
    return bool(re.search(pattern, string))
assert text_match_two_three("ac")==(False)
assert text_match_two_three("dc")==(False)
assert text_match_two_three("abbbba")==(True)