def solve(s):
    if any(c.isalpha() for c in s):
        return ''.join(c.upper() if c.islower() else c.lower() for c in s)
    return s[::-1]
    if any(c.isalpha() for c in s):
        return ''.join(c.upper() if c.islower() else c.lower() for c in s)
    else:
        return s[::-1]
def check(candidate):

    # Check some simple cases
    assert candidate("AsDf") == "aSdF"
    assert candidate("1234") == "4321"
    assert candidate("ab") == "AB"
    assert candidate("#a@C") == "#A@c"
    assert candidate("#AsdfW^45") == "#aSDFw^45"

    # Check some edge cases that are easy to work out by hand.

    # Don't remove this line:

check(solve)