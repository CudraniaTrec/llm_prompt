#Write a function to convert the given snake case string to camel case string.
import re
def snake_to_camel(word):
  return ''.join(x.capitalize() or '_' for x in word.split('_'))