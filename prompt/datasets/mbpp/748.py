#Write a function to put spaces between words starting with capital letters in a given string.
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)