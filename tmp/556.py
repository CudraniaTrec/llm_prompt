def find_Odd_Pair(arr, n):
    odd_count = 0
    even_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count * even_count
assert find_Odd_Pair([5,4,7,2,1],5) == 6
assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
assert find_Odd_Pair([1,2,3],3) == 2