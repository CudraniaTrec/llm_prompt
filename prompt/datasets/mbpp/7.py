#Write a function to find all words which are at least 4 characters long in a string.
import re
def find_char_long(text):
  return (re.findall(r"\b\w{4,}\b", text))