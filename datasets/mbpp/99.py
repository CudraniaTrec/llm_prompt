#Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
def decimal_to_binary(n): 
    return bin(n).replace("0b","") 