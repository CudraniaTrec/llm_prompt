#Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
def sample_nam(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
  return len(''.join(sample_names))