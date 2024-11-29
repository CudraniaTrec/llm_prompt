#Write a function to find the nth nonagonal number.
def is_nonagonal(n): 
	return int(n * (7 * n - 5) / 2) 