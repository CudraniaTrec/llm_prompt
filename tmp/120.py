def max_product_tuple(tuples_list):
    max_product = 0
    for tup in tuples_list:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484