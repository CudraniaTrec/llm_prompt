def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary_str = ''
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    return binary_str
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(18) == '10010'
assert decimal_to_binary(7) == '111'