#Write a function to join a list of multiple integers into a single integer.
def multiple_to_single(L):
  x = int("".join(map(str, L)))
  return x