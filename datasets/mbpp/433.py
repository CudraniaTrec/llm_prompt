#Write a function to check whether the entered number is greater than the elements of the given array.
def check_greater(arr, number):
  arr.sort()
  return number > arr[-1]