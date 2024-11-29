def replace_list(list1, list2):
    list1 = list1[:-1]  # Remove the last element of the first list
    return list1 + list2  # Concatenate the modified first list with the second list
def replace_list(list1, list2):
    list1 = list1[:-1]  # Remove the last element of the first list
    list1.extend(list2)  # Add the elements of the second list to the first list
    return list1  # Return the modified first list
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]