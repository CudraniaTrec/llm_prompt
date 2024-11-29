#Write a function to drop empty items from a given dictionary.
def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1