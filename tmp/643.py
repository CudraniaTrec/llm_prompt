def text_match_wordz_middle(s):
    if len(s) < 3:
        return False
    return 'z' in s[1:-1]
assert text_match_wordz_middle("pythonzabc.")==True
assert text_match_wordz_middle("zxyabc.")==False
assert text_match_wordz_middle("  lang  .")==False