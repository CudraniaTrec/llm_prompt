#Write a function to convert tuple string to integer tuple.
def tuple_str_int(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 