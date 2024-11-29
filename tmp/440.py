import re

def find_adverb_position(sentence):
    adverb_pattern = r'\b\w+ly\b'
    match = re.search(adverb_pattern, sentence)
    if match:
        return (match.start(), match.end(), match.group())
    return None
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')