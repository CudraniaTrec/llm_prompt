def long_words(n, sentence):
    words = sentence.split()
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list
def long_words(n, sentence):
    words = sentence.split()
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list

assert long_words(3,"python is a programming language")==['python','programming','language']
def long_words(n, sentence):
    words = sentence.split()
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list

assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(2,"writing a program")==['writing','program']
assert long_words(5,"sorting list")==['sorting']