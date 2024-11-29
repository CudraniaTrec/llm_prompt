def words_string(s):
    return [word.strip() for word in s.replace(',', ' ').split()]
    return [word.strip() for word in re.split(r'[,\s]+', s) if word]
    return [word.strip() for word in re.split(r'[,\s]+', s) if word]
    return [word.strip() for word in s.replace(',', ' ').split()]
    return [word.strip() for word in s.replace(',', ' ').split() if word.strip()]
    import re
    return re.split(r'[,\s]+', s.strip())
    return [word.strip() for word in s.replace(',', ' ').split()]
    return [word.strip() for word in s.replace(',', ' ').split() if word.strip()]
    return [word.strip() for word in re.split(r'[ ,]+', s) if word]
    return [word.strip() for word in s.replace(',', ' ').split()]
    return [word.strip() for word in re.split(r'[,\s]+', s) if word]
    import re
    return re.findall(r'\S+', s)
    return [word.strip() for word in s.replace(',', ' ').split()]
    return [word.strip() for word in re.split(',|\\s+', s) if word.strip()]
    return [word.strip() for word in s.replace(',', ' ').split() if word.strip()]
    return [word.strip() for word in re.split(r'[,\s]+', s) if word]
    return [word.strip() for word in s.replace(',', ' ').split()]
    import re
    return re.findall(r'\S+', s)
    return [word.strip() for word in s.replace(',', ' ').split()]
    import re
    return re.findall(r'\S+', s)
    return [word.strip() for word in s.replace(',', ' ').split() if word]
    return [word.strip() for word in re.split(r'[ ,]+', s) if word]
    return [word.strip() for word in re.split(r'[,\s]+', s) if word]
    return [word.strip() for word in s.replace(',', ' ').split()]
    return [word.strip() for word in s.replace(',', ' ').split()]
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert candidate("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert candidate("Hi, my name") == ["Hi", "my", "name"]
    assert candidate("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

    # Check some edge cases that are easy to work out by hand.


check(words_string)