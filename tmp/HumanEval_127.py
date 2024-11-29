def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    start_overlap = max(start1, start2)
    end_overlap = min(end1, end2)
    
    if start_overlap > end_overlap:
        return "NO"
    
    length = end_overlap - start_overlap + 1
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return "YES" if is_prime(length) else "NO"
    start1, end1 = interval1
    start2, end2 = interval2
    
    start_overlap = max(start1, start2)
    end_overlap = min(end1, end2)
    
    if start_overlap > end_overlap:
        return "NO"
    
    length = end_overlap - start_overlap + 1

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return "YES" if is_prime(length) else "NO"
def check(candidate):

    # Check some simple cases
    assert candidate((1, 2), (2, 3)) == "NO"
    assert candidate((-1, 1), (0, 4)) == "NO"
    assert candidate((-3, -1), (-5, 5)) == "YES"
    assert candidate((-2, 2), (-4, 0)) == "YES"

    # Check some edge cases that are easy to work out by hand.
    assert candidate((-11, 2), (-1, -1)) == "NO"


check(intersection)