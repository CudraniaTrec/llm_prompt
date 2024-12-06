#Write a function to find the first adverb ending with ly and its positions in a given string.
import re
def find_adverbs(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))