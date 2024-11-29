#Write a function to find the pairwise addition of the neighboring elements of the given tuple.
def add_pairwise(test_tup):
  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 