import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    min_heap = []
    result = []

    for i in range(min(k, len(nums1))):
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

    while k > 0 and min_heap:
        sum_val, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        k -= 1

    return result
assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]