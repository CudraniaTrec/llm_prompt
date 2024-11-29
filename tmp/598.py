def armstrong_number(num):
    num_str = str(num)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == num
assert armstrong_number(153)==True
assert armstrong_number(259)==False
assert armstrong_number(4458)==False