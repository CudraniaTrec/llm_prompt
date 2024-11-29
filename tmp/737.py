import re

def check_str(s):
    return bool(re.match(r'^[aeiouAEIOU]', s))
assert check_str("annie")
assert not check_str("dawood")
assert check_str("Else")