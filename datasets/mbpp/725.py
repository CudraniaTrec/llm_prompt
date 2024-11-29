#Write a function to extract values between quotation marks " " of the given string.
import re
def extract_quotation(text1):
  return (re.findall(r'"(.*?)"', text1))