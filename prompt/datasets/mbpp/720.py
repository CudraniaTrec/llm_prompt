#Write a function to add a dictionary to the tuple. The output should be a tuple.
def add_dict_to_tuple(test_tup, test_dict):
  test_tup = list(test_tup)
  test_tup.append(test_dict)
  test_tup = tuple(test_tup)
  return (test_tup) 