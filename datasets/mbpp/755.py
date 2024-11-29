#Write a function to find the second smallest number in a list.
def second_smallest(numbers):
  unique_numbers = list(set(numbers))
  unique_numbers.sort()
  if len(unique_numbers) < 2:
    return None
  else:
    return unique_numbers[1]