#Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
def dict_filter(dict,n):
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result