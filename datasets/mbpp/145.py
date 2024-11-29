#Write a python function to find the maximum difference between any two elements in a given array.
def max_Abs_Diff(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 