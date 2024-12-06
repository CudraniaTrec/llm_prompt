#Write a function to return two words from a list of words starting with letter 'p'.
import re
def start_withp(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()