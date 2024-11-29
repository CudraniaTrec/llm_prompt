#Write a function to count the number of occurence of the string 'std' in a given string.
def count_occurance(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count