#Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
def tuple_intersection(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)