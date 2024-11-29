def text_match_one(text):
    import re
    pattern = r'a(b+)'
    return bool(re.search(pattern, text))
assert text_match_one("ac")==False
assert text_match_one("dc")==False
assert text_match_one("abba")==True