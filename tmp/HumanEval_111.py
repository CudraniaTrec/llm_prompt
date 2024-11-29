
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """

    if not test:
        return {}
    
    counts = {}
    for letter in test.split():
        counts[letter] = counts.get(letter, 0) + 1

    max_count = max(counts.values())
    return {letter: count for letter, count in counts.items() if count == max_count}
    if not test:
        return {}
    counts = {}
    for letter in test.split():
        counts[letter] = counts.get(letter, 0) + 1
    max_count = max(counts.values())
    return {letter: count for letter, count in counts.items() if count == max_count}
def check(candidate):

    # Check some simple cases
    assert candidate('a b b a') == {'a':2,'b': 2}, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('a b c a b') == {'a': 2, 'b': 2}, "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "This prints if this assert fails 3 (good for debugging!)"
    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 4 (good for debugging!)"
    assert candidate('b b b b a') == {'b': 4}, "This prints if this assert fails 5 (good for debugging!)"
    
    
    # Check some edge cases that are easy to work out by hand.


check(histogram)