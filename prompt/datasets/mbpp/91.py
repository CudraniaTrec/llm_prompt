#Write a function to check if a string is present as a substring in a given list of string values.
def find_substring(str1, sub_str):
   if any(sub_str in s for s in str1):
       return True
   return False