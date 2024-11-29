#Write a function to find the cumulative sum of all the values that are present in the given tuple list.
def cummulative_sum(test_list):
  res = sum(map(sum, test_list))
  return (res)