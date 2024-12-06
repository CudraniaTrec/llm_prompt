#Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
def rear_extract(test_list):
  res = [lis[-1] for lis in test_list]
  return (res) 