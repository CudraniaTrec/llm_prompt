#Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
def find_min_diff(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 