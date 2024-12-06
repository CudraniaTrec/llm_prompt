#Write a function to get the frequency of all the elements in a list, returned as a dictionary.
import collections
def freq_count(list1):
  freq_count= collections.Counter(list1)
  return freq_count