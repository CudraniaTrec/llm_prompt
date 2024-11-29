def find_kth(arr1, arr2, k):
    len1, len2 = len(arr1), len(arr2)
    
    if len1 > len2:
        return find_kth(arr2, arr1, k)

    if len1 == 0:
        return arr2[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(len1, k // 2)
    j = min(len2, k // 2)

    if arr1[i - 1] < arr2[j - 1]:
        return find_kth(arr1[i:], arr2, k - i)
    else:
        return find_kth(arr1, arr2[j:], k - j)
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8