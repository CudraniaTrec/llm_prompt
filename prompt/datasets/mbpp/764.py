#Write a python function to count number of digits in a given string.
def number_ctr(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr