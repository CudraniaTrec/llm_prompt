
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_word = ""
    max_unique_count = 0

    for word in words:
        unique_chars = len(set(word))
        if (unique_chars > max_unique_count) or (unique_chars == max_unique_count and word < max_word):
            max_unique_count = unique_chars
            max_word = word

    return max_word
    for word in words:
        unique_chars = len(set(word))
        if (unique_chars > max_unique_count) or (unique_chars == max_unique_count and word < max_word):
            max_unique_count = unique_chars
            max_word = word
    return max_word
    for word in words:
        unique_chars = len(set(word))
        if (unique_chars > max_unique_count) or (unique_chars == max_unique_count and word < max_word):
            max_unique_count = unique_chars
            max_word = word
    return max_word
def check(candidate):

    # Check some simple cases
    assert (candidate(["name", "of", "string"]) == "string"), "t1"
    assert (candidate(["name", "enam", "game"]) == "enam"), 't2'
    assert (candidate(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
    assert (candidate(["abc", "cba"]) == "abc"), 't4'
    assert (candidate(["play", "this", "game", "of","footbott"]) == "footbott"), 't5'

    # Check some edge cases that are easy to work out by hand.


check(find_max)