#We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
def extract_index_list(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result