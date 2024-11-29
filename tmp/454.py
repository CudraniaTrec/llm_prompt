def text_match_wordz(text):
    return 'z' in text
assert text_match_wordz("pythonz.")==True
assert text_match_wordz("xyz.")==True
assert text_match_wordz("  lang  .")==False