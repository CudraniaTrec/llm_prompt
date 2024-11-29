def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    b_rotations = [b[i:] + b[:i] for i in range(len(b))]
    for rotation in b_rotations:
        if rotation in a:
            return True
    return False
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]
    return False
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("xyzw","xyw") == False , "test #0"
    assert  candidate("yello","ell") == True , "test #1"
    assert  candidate("whattup","ptut") == False , "test #2"


check(cycpattern_check)