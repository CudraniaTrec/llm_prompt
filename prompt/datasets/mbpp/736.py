#Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
import bisect
def left_insertion(a, x):
    i = bisect.bisect_left(a, x)
    return i