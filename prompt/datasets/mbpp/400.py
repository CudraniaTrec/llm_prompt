#Write a function to extract the number of unique tuples in the given list.
def extract_freq(test_list):
  res = len(list(set(tuple(sorted(sub)) for sub in test_list)))
  return (res)