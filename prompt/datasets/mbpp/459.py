#Write a function to remove uppercase substrings from a given string.
import re
def remove_uppercase(str1):
  return re.sub('[A-Z]', '', str1)