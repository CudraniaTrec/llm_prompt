def large_product(list1, list2, n):
    products = []
    for x in list1:
        for y in list2:
            products.append(x * y)
    products = sorted(products, reverse=True)
    return products[:n]
def large_product(list1, list2, n):
    products = []
    for x in list1:
        for y in list2:
            products.append(x * y)
    products = sorted(products, reverse=True)
    return products[:n]

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
def large_product(list1, list2, n):
    products = []
    for x in list1:
        for y in list2:
            products.append(x * y)
    products = sorted(products, reverse=True)
    return products[:n]

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]