#Write a function to replace all occurrences of spaces, commas, or dots with a colon.
import re
def replace_specialchar(text):
 return (re.sub("[ ,.]", ":", text))
