#Write a python function to check if the elements of a given list are unique or not.
def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True