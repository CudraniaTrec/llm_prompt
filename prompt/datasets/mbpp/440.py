#Write a function to find the first adverb and their positions in a given sentence.
import re
def find_adverb_position(text):
 for m in re.finditer(r"\w+ly", text):
    return (m.start(), m.end(), m.group(0))