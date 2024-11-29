#Write a function to find the maximum difference between available pairs in the given tuple list.
def max_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = max(temp)
  return (res) 