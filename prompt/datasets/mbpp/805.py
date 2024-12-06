#Write a function that returns the list in a list of lists whose sum of elements is the highest.
def max_sum_list(lists):
 return max(lists, key=sum)