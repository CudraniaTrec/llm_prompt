#Write a function to find the union of the elements of two given tuples and output them in sorted order.
def union_elements(test_tup1, test_tup2):
  res = tuple(set(test_tup1 + test_tup2))
  return (res) 