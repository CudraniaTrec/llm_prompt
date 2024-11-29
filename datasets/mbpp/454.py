#Write a function that matches a word containing 'z'.
import re
def text_match_wordz(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return True
        else:
                return False