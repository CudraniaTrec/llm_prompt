#Write a function to locate the right insertion point for a specified value in sorted order.
import bisect
def right_insertion(a, x):
    return bisect.bisect_right(a, x)