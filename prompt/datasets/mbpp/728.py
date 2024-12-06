#Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
def sum_list(lst1,lst2):
  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 
  return res_list