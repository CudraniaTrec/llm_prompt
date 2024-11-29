def find_Element(arr, rotations, n, r):
    for i in range(r):
        rotation = rotations[i]
        step, index = rotation
        # Perform the rotation
        arr = arr[step:] + arr[:step]
    # Return the element at the specified index
    return arr[index]
def find_Element(arr, rotations, n, r):
    for i in range(r):
        rotation = rotations[i]
        step, index = rotation
        # Perform the rotation
        arr = arr[step:] + arr[:step]
    # Return the element at the specified index
    return arr[index]

assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
def find_Element(arr, rotations, n, r):
    for i in range(r):
        rotation = rotations[i]
        step, index = rotation
        # Perform the rotation
        arr = arr[step:] + arr[:step]
    # Return the element at the specified index
    return arr[index]

assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
def find_Element(arr, rotations, n, r):
    for i in range(r):
        rotation = rotations[i]
        step, index = rotation
        # Perform the rotation
        arr = arr[step:] + arr[:step]
    # Return the element at the specified index
    return arr[index]

assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1