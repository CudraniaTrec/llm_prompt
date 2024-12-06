#Write a function to check if all values are same in a dictionary.
def check_value(dict, n):
    result = all(x == n for x in dict.values()) 
    return result