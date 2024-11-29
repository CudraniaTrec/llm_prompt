#Write a function to check whether the product of numbers in a list is even or not.
def is_product_even(arr): 
    for i in range(len(arr)): 
        if (arr[i] & 1) == 0: 
            return True
    return False