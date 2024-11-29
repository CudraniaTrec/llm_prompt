#Write a python function to return the negative numbers in a list.
def neg_nos(list1):
  out = []
  for num in list1: 
    if num < 0: 
      out.append(num)
  return out 