def second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
assert second_smallest([2,2])==None
assert second_smallest([2,2,2])==None