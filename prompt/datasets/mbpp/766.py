#Write a function to return a list of all pairs of consecutive items in a given list.
def pair_wise(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp