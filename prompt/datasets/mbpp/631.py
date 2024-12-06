#Write a function to replace whitespaces with an underscore and vice versa in a given string.
def replace_spaces(text):
  return "".join(" " if c == "_" else ("_" if c == " " else c) for c in text)