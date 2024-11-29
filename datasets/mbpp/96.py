#Write a python function to find the number of divisors of a given integer.
def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x