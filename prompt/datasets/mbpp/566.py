#Write a function to get the sum of the digits of a non-negative integer.
def sum_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))