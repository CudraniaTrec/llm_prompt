def next_smallest_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    
    n += 1
    while not is_palindrome(n):
        n += 1
    return n
assert next_smallest_palindrome(99)==101
assert next_smallest_palindrome(1221)==1331
assert next_smallest_palindrome(120)==121