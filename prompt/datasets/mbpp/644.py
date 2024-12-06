#Write a python function to reverse an array upto a given position.
def reverse_Array_Upto_K(input, k): 
  return (input[k-1::-1] + input[k:]) 