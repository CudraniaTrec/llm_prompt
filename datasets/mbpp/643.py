#Write a function that checks if a strings contains 'z', except at the start and end of the word.
import re
def text_match_wordz_middle(text):
        return bool(re.search(r'\Bz\B',  text))