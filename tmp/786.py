def right_insertion(sorted_list, value):
    for index, current in enumerate(sorted_list):
        if current > value:
            return index
    return len(sorted_list)
assert right_insertion([1,2,4,5],6)==4
assert right_insertion([1,2,4,5],3)==2
assert right_insertion([1,2,4,5],7)==4