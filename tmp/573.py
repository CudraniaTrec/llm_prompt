def unique_product(numbers):
    unique_numbers = set(numbers)
    product = 1
    for num in unique_numbers:
        product *= num
    return product
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
assert unique_product([1, 2, 3, 1,]) == 6
assert unique_product([7, 8, 9, 0, 1, 1]) == 0