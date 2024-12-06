#Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
import re

def find_literals(text, pattern):
  match = re.search(pattern, text)
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)