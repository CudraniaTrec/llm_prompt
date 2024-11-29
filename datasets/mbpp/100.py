#Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
import sys
def next_smallest_palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i