#Write a function to count the number of occurrences of a number in a given list.
def frequency(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count += 1

    return count 