#Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])