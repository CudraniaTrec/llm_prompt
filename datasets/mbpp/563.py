#Write a function to extract values between quotation marks from a string.
import re
def extract_values(text):
 return (re.findall(r'"(.*?)"', text))