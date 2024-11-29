#Write a function to find the n largest integers from a given list of numbers, returned in descending order.
import heapq as hq
def heap_queue_largest(nums,n):
  largest_nums = hq.nlargest(n, nums)
  return largest_nums