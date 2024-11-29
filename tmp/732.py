def replace_specialchar(text):
    return text.replace(' ', ':').replace(',', ':').replace('.', ':')
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')