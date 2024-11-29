#Write a python function to find the sum of the per-digit difference between two integers.
def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))