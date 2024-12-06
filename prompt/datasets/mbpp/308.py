#Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
def large_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
    return result