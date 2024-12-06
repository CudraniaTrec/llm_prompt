#Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
def find_solution(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None