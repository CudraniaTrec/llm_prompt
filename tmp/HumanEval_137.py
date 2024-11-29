def compare_one(a, b):
    def parse_number(val):
        if isinstance(val, str):
            val = val.replace(',', '.')  # Replace commas with dots
        return float(val)

    a_parsed = parse_number(a)
    b_parsed = parse_number(b)
    
    if a_parsed == b_parsed:
        return None
    
    return a if a_parsed > b_parsed else b
def parse_number(val):
    if isinstance(val, str):
        val = val.replace(',', '.')
    return float(val)

a_parsed = parse_number(a)
b_parsed = parse_number(b)

if a_parsed == b_parsed:
    return None

return a if a_parsed > b_parsed else b
    def parse_number(x):
        if isinstance(x, str):
            x = x.replace(",", ".")
        return float(x)

    a_parsed = parse_number(a)
    b_parsed = parse_number(b)

    if a_parsed == b_parsed:
        return None
    return a if a_parsed > b_parsed else b
def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"

    # Check some edge cases that are easy to work out by hand.


check(compare_one)