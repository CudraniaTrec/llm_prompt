#Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
import re
def occurance_substring(text,pattern):
 for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    return (text[s:e], s, e)