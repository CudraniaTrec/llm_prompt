#Write a function to extract only the rear index element of each string in the given tuple.
def extract_rear(test_tuple):
  res = list(sub[len(sub) - 1] for sub in test_tuple)
  return (res) 