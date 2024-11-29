from fractions import Fraction

def simplify(x, n):
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
    fraction_x = Fraction(x)
    fraction_n = Fraction(n)
    result = fraction_x * fraction_n
    return result.denominator == 1
def check(candidate):

    # Check some simple cases
    assert candidate("1/5", "5/1") == True, 'test1'
    assert candidate("1/6", "2/1") == False, 'test2'
    assert candidate("5/1", "3/1") == True, 'test3'
    assert candidate("7/10", "10/2") == False, 'test4'
    assert candidate("2/10", "50/10") == True, 'test5'


    # Check some edge cases that are easy to work out by hand.


check(simplify)