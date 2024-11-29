

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9 inclusive.")
    
    if x == 0:
        return '0'
    
    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base
    
    return result


METADATA = {}


def check(candidate):
    assert candidate(8, 3) == "22"
    assert candidate(9, 3) == "100"
    assert candidate(234, 2) == "11101010"
    assert candidate(16, 2) == "10000"
    assert candidate(8, 2) == "1000"
    for x in range(2, 8):


check(change_base)