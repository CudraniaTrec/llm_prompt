#Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest