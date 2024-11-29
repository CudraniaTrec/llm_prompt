def is_undulating(number):
    number_str = str(number)
    for i in range(1, len(number_str)):
        if number_str[i] == number_str[i - 1]:
            return False
    return True
def is_undulating(number):
    number_str = str(number)
    for i in range(1, len(number_str)):
        if number_str[i] == number_str[i - 1]:
            return False
    return True

assert is_undulating(1212121) == True
assert is_undulating(1212121) == True
assert is_undulating(1991) == False
assert is_undulating(121) == True