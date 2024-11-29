#Write a function to reverse each string in a given list of string values.
def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result