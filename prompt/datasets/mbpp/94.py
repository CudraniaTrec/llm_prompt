#Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
from operator import itemgetter 
def index_minimum(test_list):
  res = min(test_list, key = itemgetter(1))[0]
  return (res) 