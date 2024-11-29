def catalan_number(n):
    # Initialize a list to store computed Catalan numbers
    catalan = [0] * (n + 1)
    # The first Catalan number is 1
    catalan[0] = 1
    # Calculate Catalan numbers using the formula
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    # Return the nth Catalan number
    return catalan[n]
assert catalan_number(10)==16796
assert catalan_number(9)==4862
assert catalan_number(7)==429