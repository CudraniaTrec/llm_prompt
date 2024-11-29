def recursive_list_sum(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210