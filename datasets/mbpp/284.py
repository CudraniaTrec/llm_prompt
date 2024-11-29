#Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
def check_element(list,element):
  check_element=all(v== element for v in list)
  return check_element