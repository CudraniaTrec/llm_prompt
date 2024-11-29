def replace_blank(input_string, replace_char):
    return input_string.replace(' ', replace_char)
assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("python program language",'$')==("python$program$language")
assert replace_blank("blank space","-")==("blank-space")