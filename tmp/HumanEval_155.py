
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)
    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)
    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)
    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)
    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)
    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)
def check(candidate):

    # Check some simple cases
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)


    # Check some edge cases that are easy to work out by hand.


check(even_odd_count)