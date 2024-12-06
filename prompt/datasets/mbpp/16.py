#Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
import re
def text_lowercase_underscore(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return True
        else:
                return False