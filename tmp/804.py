def is_product_even(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product % 2 == 0
assert is_product_even([1,2,3])
assert is_product_even([1,2,1,4])
assert not is_product_even([1,1])