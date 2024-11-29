def positive_count(arr):
    total_count = len(arr)
    if total_count == 0:
        return 0.0
    positive_numbers = sum(1 for x in arr if x > 0)
    return positive_numbers / total_count
def positive_count(arr):
    total_count = len(arr)
    if total_count == 0:
        return 0.0
    positive_numbers = sum(1 for x in arr if x > 0)
    return round(positive_numbers / total_count, 2)
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56