def power_base_sum(base, power):
    # Calculate the base raised to the given power
    result = base ** power
    # Convert the result to a string and sum its digits
    digit_sum = sum(int(digit) for digit in str(result))
    return digit_sum
assert power_base_sum(2,100)==115
assert power_base_sum(8,10)==37
assert power_base_sum(8,15)==62
assert power_base_sum(3,3)==9