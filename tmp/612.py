def merge(lst):
    first_elements = []
    second_elements = []
    for sublist in lst:
        first_elements.append(sublist[0])
        second_elements.append(sublist[1])
    return [first_elements, second_elements]
def merge(lst):
    first_elements = []
    second_elements = []
    for sublist in lst:
        first_elements.append(sublist[0])
        second_elements.append(sublist[1])
    return [first_elements, second_elements]

assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]