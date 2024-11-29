#Write a function to find tuples which have all elements divisible by k from the given list of tuples.
def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return res