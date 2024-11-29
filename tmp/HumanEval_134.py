
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''

    if not txt:  # Check if the string is empty
        return False
    
    txt = txt.rstrip()  # Remove trailing spaces
    if len(txt) == 0:  # Check if the string is empty after stripping
        return False
    
    last_char = txt[-1]  # Get the last character
    if last_char.isalpha():  # Check if it's an alphabetical character
        if txt[-2] == ' ' or len(txt) == 1:  # Ensure it's not part of a word
            return True

    return False
    if not txt:  # Check if the string is empty
        return False
    txt = txt.rstrip()  # Remove trailing spaces
    if len(txt) == 0:  # Check if the string is empty after stripping
        return False
    last_char = txt[-1]  # Get the last character
    if last_char.isalpha():  # Check if it's an alphabetical character
        if txt[-2] == ' ' or len(txt) == 1:  # Ensure it's not part of a word
            return True
    return False
def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False

    # Check some edge cases that are easy to work out by hand.


check(check_if_last_char_is_a_letter)