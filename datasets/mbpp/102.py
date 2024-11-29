#Write a function to convert a snake case string to camel case string.
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))