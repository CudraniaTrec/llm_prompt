#Write a function to create a list of N empty dictionaries.
def empty_list(length):
 empty_list = [{} for _ in range(length)]
 return empty_list