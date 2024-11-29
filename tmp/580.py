def extract_even(nested_tuple):
    result = []
    
    for element in nested_tuple:
        if isinstance(element, tuple):
            even_element = extract_even(element)
            if even_element:  # Only add if it's not empty
                result.append(even_element)
        elif isinstance(element, int) and element % 2 == 0:
            result.append(element)
    
    return tuple(result)
def extract_even(nested_tuple):
    result = []
    
    for element in nested_tuple:
        if isinstance(element, tuple):
            even_element = extract_even(element)
            if even_element:  # Only add if it's not empty
                result.append(even_element)
        elif isinstance(element, int) and element % 2 == 0:
            result.append(element)
    
    return tuple(result)

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
def extract_even(nested_tuple):
    result = []
    
    for element in nested_tuple:
        if isinstance(element, tuple):
            even_element = extract_even(element)
            if even_element:  # Only add if it's not empty
                result.append(even_element)
        elif isinstance(element, int) and element % 2 == 0:
            result.append(element)
    
    return tuple(result)

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)