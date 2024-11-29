def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)
    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
def check(candidate):

    # Check some simple cases
    assert candidate(123) == (8, 13)
    assert candidate(12) == (4, 6)
    assert candidate(3) == (1, 2)
    assert candidate(63) == (6, 8)
    assert candidate(25) == (5, 6)

    # Check some edge cases that are easy to work out by hand.


check(even_odd_palindrome)