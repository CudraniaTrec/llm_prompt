#Write a function to compute the sum of digits of each number of a given list.
def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())