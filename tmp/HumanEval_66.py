
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """

    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(c) for c in s if c.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
    return sum(ord(char) for char in s if char.isupper())
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("") == 0, "Error"
    assert candidate("abAB") == 131, "Error"
    assert candidate("abcCd") == 67, "Error"
    assert candidate("helloE") == 69, "Error"

    # Check some edge cases that are easy to work out by hand.


check(digitSum)