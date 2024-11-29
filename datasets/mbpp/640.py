#Write a function to remove the parenthesis and what is inbetween them from a string.
import re
def remove_parenthesis(items):
 for item in items:
    return (re.sub(r" ?\([^)]+\)", "", item))