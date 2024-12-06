#Write a python function to split a list at the nth eelment and add the first part to the end.
def split_Arr(l, n):
  return l[n:] + l[:n]