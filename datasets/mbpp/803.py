#Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
def is_perfect_square(n) :
    i = 1
    while (i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True     
        i = i + 1
    return False