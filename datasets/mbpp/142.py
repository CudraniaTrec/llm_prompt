#Write a function to count number items that are identical in the same position of three given lists.
def count_samepair(list1,list2,list3):
    result = sum(m == n == o for m, n, o in zip(list1,list2,list3))
    return result