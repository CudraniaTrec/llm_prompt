def min_product_tuple(tuples_list):
    min_product = float('inf')
    for tup in tuples_list:
        product = tup[0] * tup[1]
        if product < min_product:
            min_product = product
    return min_product
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100