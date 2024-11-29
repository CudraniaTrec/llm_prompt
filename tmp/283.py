def validate(n):
    from collections import Counter
    
    # Convert the integer to string to iterate over digits
    str_n = str(n)
    
    # Count the frequency of each digit
    freq = Counter(str_n)
    
    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, count in freq.items():
        if count > int(digit):
            return False
    return True
assert validate(1234) == True
assert validate(51241) == False
assert validate(321) == True