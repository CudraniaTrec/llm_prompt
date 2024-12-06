#Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
def substract_elements(test_tup1, test_tup2):
  res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))
  return (res) 