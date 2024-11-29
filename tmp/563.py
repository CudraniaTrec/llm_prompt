def extract_values(s):
    import re
    matches = re.findall(r'"(.*?)"', s)
    return matches
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
assert extract_values('"python","program","language"')==['python','program','language']
assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']