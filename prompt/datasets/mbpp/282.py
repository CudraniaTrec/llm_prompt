#Write a function to subtract two lists element-wise.
def sub_list(nums1,nums2):
  result = map(lambda x, y: x - y, nums1, nums2)
  return list(result)