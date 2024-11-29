#Write a python function to count the number of rotations required to generate a sorted array. https://www.geeksforgeeks.org/count-of-rotations-required-to-generate-a-sorted-array/
def count_rotation(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0