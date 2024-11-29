
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

    text = text.replace('  ', '-').replace(' ', '_')
    return text
    import re
    text = re.sub(r'\s{3,}', '-', text)  # Replace 3 or more spaces with '-'
    text = text.replace(' ', '_')         # Replace remaining spaces with '_'
    return text
    text = text.replace('  ', '-')
    text = text.replace(' ', '_')
    return text
    text = ' '.join(text.split())
    if ' ' in text and text.count(' ') > 2:
        text = text.replace(' ', '-')
    else:
        text = text.replace(' ', '_')
    return text
    text = ' '.join(text.split())
    if ' ' in text and text.count(' ') > 2:
        text = text.replace(' ', '-')
    else:
        text = text.replace(' ', '_')
    return text
def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)