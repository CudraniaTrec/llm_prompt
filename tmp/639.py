def sample_nam(names):
    filtered_names = [name for name in names if not name[0].islower()]
    total_length = sum(len(name) for name in filtered_names)
    return total_length
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
assert sample_nam(["abcd", "Python", "abba", "aba"])==6