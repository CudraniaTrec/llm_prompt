#Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
def count_reverse_pairs(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res