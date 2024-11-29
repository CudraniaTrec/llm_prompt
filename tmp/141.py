def pancake_sort(arr):
    def flip(sub_arr, k):
        return sub_arr[:k][::-1] + sub_arr[k:]

    n = len(arr)
    for i in range(n, 1, -1):
        max_index = arr.index(max(arr[:i]))
        if max_index != i - 1:
            if max_index != 0:
                arr = flip(arr, max_index + 1)
            arr = flip(arr, i)
    return arr
def pancake_sort(arr):
    def flip(sub_arr, k):
        return sub_arr[:k][::-1] + sub_arr[k:]

    n = len(arr)
    for i in range(n, 1, -1):
        max_index = arr.index(max(arr[:i]))
        if max_index != i - 1:
            if max_index != 0:
                arr = flip(arr, max_index + 1)
            arr = flip(arr, i)
    return arr

assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
def pancake_sort(arr):
    def flip(sub_arr, k):
        return sub_arr[:k][::-1] + sub_arr[k:]

    n = len(arr)
    for i in range(n, 1, -1):
        max_index = arr.index(max(arr[:i]))
        if max_index != i - 1:
            if max_index != 0:
                arr = flip(arr, max_index + 1)
            arr = flip(arr, i)
    return arr

assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]