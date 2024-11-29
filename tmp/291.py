def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k

    prev2 = k  # ways to paint last post with different color from previous
    prev1 = k * k  # ways to paint last post with the same color as previous post
    current = 0
    
    for i in range(3, n + 1):
        current = (k - 1) * (prev1 + prev2)
        prev2 = prev1
        prev1 = current
    
    return current
def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k

    prev2 = k  # ways to paint last post with different color from previous
    prev1 = k * k  # ways to paint last post with the same color as previous post
    current = 0
    
    for i in range(3, n + 1):
        current = (k - 1) * (prev1 + prev2)
        prev2 = prev1
        prev1 = current
    
    return current

assert count_no_of_ways(2, 4) == 16
assert count_no_of_ways(2, 4) == 16
assert count_no_of_ways(3, 2) == 6
assert count_no_of_ways(4, 4) == 228