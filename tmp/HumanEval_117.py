def select_words(s, n):
    if not s:
        return []
    
    vowels = "aeiouAEIOU"
    words = s.split()
    result = []
    
    for word in words:
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)
    
    return result
    for word in words:
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)
    return result
    for word in words:
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)
    return result
    if not s:
        return []

    vowels = "aeiouAEIOU"
    words = s.split()
    result = []

    for word in words:
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)

    return result
def check(candidate):

    # Check some simple cases
    assert candidate("Mary had a little lamb", 4) == ["little"], "First test error: " + str(candidate("Mary had a little lamb", 4))      
    assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"], "Second test error: " + str(candidate("Mary had a little lamb", 3))  
    assert candidate("simple white space", 2) == [], "Third test error: " + str(candidate("simple white space", 2))      
    assert candidate("Hello world", 4) == ["world"], "Fourth test error: " + str(candidate("Hello world", 4))  
    assert candidate("Uncle sam", 3) == ["Uncle"], "Fifth test error: " + str(candidate("Uncle sam", 3))


    # Check some edge cases that are easy to work out by hand.


check(select_words)