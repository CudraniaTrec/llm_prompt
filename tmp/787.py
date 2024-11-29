import re

def text_match_three(text):
    pattern = r'a[b]{3}'
    return bool(re.fullmatch(pattern, text))
assert not text_match_three("ac")
assert not text_match_three("dc")
assert text_match_three("abbbba")
assert text_match_three("caacabbbba")