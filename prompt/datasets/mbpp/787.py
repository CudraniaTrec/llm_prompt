#Write a function that matches a string that has an a followed by three 'b'.
import re
def text_match_three(text):
        patterns = 'ab{3}?'
        return re.search(patterns,  text)