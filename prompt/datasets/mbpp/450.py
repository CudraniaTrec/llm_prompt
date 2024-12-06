#Write a function to extract specified size of strings from a given list of string values.
def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result