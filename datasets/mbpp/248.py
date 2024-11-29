#Write a function that takes in an integer n and calculates the harmonic sum of n-1.
def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1)) 