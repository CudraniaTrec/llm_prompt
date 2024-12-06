#Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
def replace_list(list1,list2):
 list1[-1:] = list2
 replace_list=list1
 return replace_list
