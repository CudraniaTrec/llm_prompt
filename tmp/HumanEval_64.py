
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    return sum(1 for i in s.lower() if i in 'aeiou' or (i == 'y' and s[-1].lower() == 'y'))
    return sum(1 for i in s.lower() if i in 'aeiou' or (i == 'y' and s[-1].lower() == 'y'))
    return sum(1 for i in s.lower() if i in 'aeiou' or (i == 'y' and s[-1].lower() == 'y'))
    return sum(1 for i in s.lower() if i in 'aeiou' or (i == 'y' and s[-1].lower() == 'y'))
    return sum(1 for i in s.lower() if i in 'aeiou' or (i == 'y' and s[-1].lower() == 'y'))
    return sum(1 for i in s.lower() if i in 'aeiou') + (1 if s.lower().endswith('y') else 0)
def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("key") == 2, "Test 3"
    assert candidate("bye") == 1, "Test 4"
    assert candidate("keY") == 2, "Test 5"

    # Check some edge cases that are easy to work out by hand.


check(vowels_count)