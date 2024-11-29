import re

def text_match_zero_one(string):
    pattern = r"a(b+)"
    if re.search(pattern, string):
        return True
    else:
        return False
assert text_match_zero_one("ac")==False
assert text_match_zero_one("dc")==False
assert text_match_zero_one("abbbba")==True
assert text_match_zero_one("dsabbbba")==True
assert text_match_zero_one("asbbbba")==False