#Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
import re
def text_match_two_three(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return True
        else:
                return False