#Write a function to divide two lists element wise.
def div_list(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, nums2)
  return list(result)