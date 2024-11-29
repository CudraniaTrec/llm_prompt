def find_sum(lst):
    unique_elements = set()
    repeated_elements = set()
    
    for num in lst:
        if num in unique_elements:
            repeated_elements.add(num)
        else:
            unique_elements.add(num)
    
    unique_elements -= repeated_elements
    
    return sum(unique_elements)
def find_sum(lst):
    unique_elements = set()
    repeated_elements = set()
    
    for num in lst:
        if num in unique_elements:
            repeated_elements.add(num)
        else:
            unique_elements.add(num)
    
    unique_elements -= repeated_elements
    
    return sum(unique_elements)

assert find_sum([1,2,3,1,1,4,5,6]) == 21
assert find_sum([1,2,3,1,1,4,5,6]) == 21
assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
assert find_sum([12,10,9,45,2,10,10,45,10]) == 78