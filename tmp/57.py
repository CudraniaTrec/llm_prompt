def find_Max_Num(digits):
    # Convert digits to strings for sorting
    digits_str = list(map(str, digits))
    # Sort the strings in descending order
    digits_str.sort(reverse=True, key=lambda x: x*10)
    # Join the sorted strings and convert back to an integer
    return int(''.join(digits_str))
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,1]) == 6541
assert find_Max_Num([1,2,3,9]) == 9321