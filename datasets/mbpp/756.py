#Write a function that matches a string that has an 'a' followed by one or more 'b's. https://www.w3resource.com/python-exercises/re/python-re-exercise-3.php
import re
def text_match_zero_one(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return True
        else:
                return False