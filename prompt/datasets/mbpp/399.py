#Write a function to perform the mathematical bitwise xor operation across the given tuples.
def bitwise_xor(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 