def text_starta_endb(s):
    return s.startswith('a') and s.endswith('b')
assert text_starta_endb("aabbbb")
assert not text_starta_endb("aabAbbbc")
assert not text_starta_endb("accddbbjjj")