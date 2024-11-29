def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "AEIOUaeiou"
    closest_vowel = ""
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i + 1].isalpha() and word[i - 1].isalpha() and word[i + 1] not in vowels and word[i - 1] not in vowels:
                closest_vowel = word[i]
                break
    
    return closest_vowel
    vowels = "AEIOUaeiou"
    closest_vowel = ""
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if i + 1 < len(word) and i - 1 >= 0:
                if word[i + 1].isalpha() and word[i - 1].isalpha() and \
                   word[i + 1] not in vowels and word[i - 1] not in vowels:
                    closest_vowel = word[i]
                    break
    
    return closest_vowel
def check(candidate):

    # Check some simple cases
    assert candidate("yogurt") == "u"
    assert candidate("full") == "u"
    assert candidate("easy") == ""
    assert candidate("eAsy") == ""
    assert candidate("ali") == ""

    # Check some edge cases that are easy to work out by hand.


check(get_closest_vowel)