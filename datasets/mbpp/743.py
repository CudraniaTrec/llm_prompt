#Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
def rotate_right(list, m):
  result =  list[-m:] + list[:-m]
  return result