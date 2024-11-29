
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2  # 1 and 1

    start_count = 10**(n - 1) - 10**(n - 2)  # Numbers starting with 1
    end_count = 10**(n - 1)  # Numbers ending with 1

    total_count = start_count + end_count - 10**(n - 2)  # Subtract overlap
    return total_count
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800

    # Check some edge cases that are easy to work out by hand.


check(starts_one_ends)