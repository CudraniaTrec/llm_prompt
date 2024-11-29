def is_simple_power(x, n):
    if n <= 1:
        return x == 1
    power = 0
    while True:
        result = n ** power
        if result == x:
            return True
        elif result > x:
            return False
        power += 1
    if n <= 1:
        return x == 1
    power = 0
    while True:
        result = n ** power
        if result == x:
            return True
        elif result > x:
            return False
        power += 1
    if n <= 1:
        return x == 1
    power = 0
    while True:
        result = n ** power
        if result == x:
            return True
        elif result > x:
            return False
        power += 1
def check(candidate):

    # Check some simple cases
    assert candidate(16, 2)== True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(143214, 16)== False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(4, 2)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(9, 3)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(16, 4)==True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.


check(is_simple_power)