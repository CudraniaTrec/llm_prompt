#Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
def max_of_nth(test_list, N):
  res = max([sub[N] for sub in test_list])
  return (res) 