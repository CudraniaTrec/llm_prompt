#Write a python function to remove odd numbers from a given list.
def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l