def last_Digit_Factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial % 10
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(21) == 0
assert last_Digit_Factorial(30) == 0