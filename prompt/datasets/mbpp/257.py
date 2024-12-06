#Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
def swap_numbers(a,b):
 temp = a
 a = b
 b = temp
 return (a,b)