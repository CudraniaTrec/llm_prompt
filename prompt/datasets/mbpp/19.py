#Write a function to find whether a given array of integers contains any duplicate element.
def test_duplicate(arraynums):
    nums_set = set(arraynums)    
    return len(arraynums) != len(nums_set)     