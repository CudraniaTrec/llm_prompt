#Write a python function to find the sum of even numbers at even positions of a list.
def sum_even_and_even_index(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum