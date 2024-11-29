import math
def babylonian_squareroot(n):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number.")
    guess = n / 2.0
    while True:
        next_guess = (guess + n / guess) / 2.0
        if abs(guess - next_guess) < 1e-10:  # convergence criteria
            return next_guess
        guess = next_guess
assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)