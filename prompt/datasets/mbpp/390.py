#Write a function to apply a given format string to all of the elements in a list.
def add_string(list_, string):
 add_string=[string.format(i) for i in  list_]
 return add_string