#Write a function to find the dissimilar elements in the given two tuples.
def find_dissimilar(test_tup1, test_tup2):
  res = tuple(set(test_tup1) ^ set(test_tup2))
  return (res) 