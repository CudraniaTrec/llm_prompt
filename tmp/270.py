def sum_even_and_even_index(lst):
    total = 0
    for index in range(len(lst)):
        if index % 2 == 0 and lst[index] % 2 == 0:
            total += lst[index]
    return total
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
assert sum_even_and_even_index([5, 6, 12, 1]) == 12