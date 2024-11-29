def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if not name or not name[0].isalpha():
        return 'No'
    
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    digit_count = sum(1 for char in file_name if char.isdigit())
    
    if digit_count > 3:
        return 'No'
    
    return 'Yes'
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if not name or not name[0].isalpha():
        return 'No'
    
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    digit_count = sum(1 for char in file_name if char.isdigit())
    
    if digit_count > 3:
        return 'No'
    
    return 'Yes'
def check(candidate):

    # Check some simple cases
    assert candidate("example.txt") == 'Yes'
    assert candidate("1example.dll") == 'No'
    assert candidate('s1sdf3.asd') == 'No'
    assert candidate('K.dll') == 'Yes'
    assert candidate('MY16FILE3.exe') == 'Yes'
    
        

    # Check some edge cases that are easy to work out by hand.


check(file_name_check)