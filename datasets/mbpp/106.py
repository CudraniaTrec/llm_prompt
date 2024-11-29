#Write a function to append the given list to the given tuples.
def add_lists(test_list, test_tup):
  res = tuple(list(test_tup) + test_list)
  return (res) 