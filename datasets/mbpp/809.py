#Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
def check_smaller(test_tup1, test_tup2):
  return all(x > y for x, y in zip(test_tup1, test_tup2))