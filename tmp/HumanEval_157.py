
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
sides = sorted([a, b, c])
return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 3) == False
    assert candidate(10, 6, 8) == True
    assert candidate(2, 2, 2) == False
    assert candidate(7, 24, 25) == True

    # Check some edge cases that are easy to work out by hand.


check(right_angle_triangle)